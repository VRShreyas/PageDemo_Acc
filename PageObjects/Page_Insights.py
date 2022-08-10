from selenium.webdriver.common.by import By


class Insights_5G_Page:

    def __init__(self, driverC):
        self.driver = driverC

    Text_5G = (By.XPATH, "//div/h1[contains(text(),'The future is 5G')]")

    def Text_5G_InsightsPage(self):
        return self.driver.find_element(*Insights_5G_Page.Text_5G)
