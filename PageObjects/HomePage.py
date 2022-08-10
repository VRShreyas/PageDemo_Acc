from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driverC):
        self.driver = driverC
        # constructor is created which accepts-driverC from test_Page_5G

    InsightOption = (By.XPATH, "//span[contains(text(),'Insights')]")
    InsightFeatures = (By.XPATH, "//div/div[1]/ul[2][@class='no-l3 secondaryCounter col-sm-8']")

    def InsightOption_CLick(self):
        return self.driver.find_element(*HomePage.InsightOption)

    def InsightFeature_List(self):
        return self.driver.find_elements(*HomePage.InsightFeatures)
