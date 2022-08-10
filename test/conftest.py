import pytest as pytest
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import time


# 1.Direct to Site.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope="class")
def setUp1(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driverC = webdriver.Chrome(executable_path="C:\\ZzDrivers\\chromedriver.exe")
        driverC.get("https://www.accenture.com/in-en")
        driverC.maximize_window()
    elif browser_name == "firefox":
        driverC = webdriver.Firefox(executable_path="C:\\ZzDrivers\\geckodriver.exe")
        driverC.get("https://www.accenture.com/in-en")
        driverC.maximize_window()
    # 1.we use request as an instance and tie up to class
    # 2.Assigning the local driver of fixture to class driver
    request.cls.driverC = driverC
    yield
    time.sleep(6)
    driverC.close()
