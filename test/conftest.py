import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.service import Service

driverC = None


# 1.Direct to Site.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


accentureURL = "https://www.accenture.com/in-en"


@pytest.fixture(scope="class")
def setUp1(request):
    global driverC
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driverC = webdriver.Chrome(executable_path="C:\\ZzDrivers\\chromedriver.exe")
        driverC.get(accentureURL)
        driverC.maximize_window()
    elif browser_name == "firefox":
        driverC = webdriver.Firefox(executable_path="C:\\ZzDrivers\\geckodriver.exe")
        driverC.get(accentureURL)
        driverC.maximize_window()

    elif browser_name == "edge":
        driverC = webdriver.Edge(service=Service("C:\\ZzDrivers\\msedgedriver.exe"))
        # driverC.implicitly_wait(10)
        driverC.get("https://www.amazon.in/")
        driverC.maximize_window()
    # 1.we use request as an instance and tie up to class
    # 2.Assigning the local driver of fixture to class driver
    request.cls.driverC = driverC
    yield
    time.sleep(6)
    driverC.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    # timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield

    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".PNG"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(name):
    driverC.get_screenshot_as_file(name)
