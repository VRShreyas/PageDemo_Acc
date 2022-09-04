import time

from selenium.webdriver.common.by import By

from PageObjects.HomePage import HomePage
from PageObjects.Page_Insights import Insights_5G_Page
from Utilities.BaseClass import BaseClass


class Test_5GPage(BaseClass):

    def test_page_5G(self):
        log1 = self.getLogger()
        HomePage1 = HomePage(self.driverC)  # create object wrt HomePage,
        HomePage1.InsightOption_CLick().click()  # Click on the Insights option
        log1.info("Insight option is clicked successfully.")
        time.sleep(4)
        # 2.Select the locator for Insights in page.
        InsightFeatures_List = HomePage1.InsightFeature_List()
        for eachInsightFeatureList in InsightFeatures_List:
            InsightFeatureName = eachInsightFeatureList.find_element(By.XPATH, 'li[1]/a').text
            if InsightFeatureName == "5G":
                log1.info("The selected option is 5G")
                eachInsightFeatureList.find_element(By.XPATH, 'li[1]/a').click()
                log1.info("5G page button  is clicked successfully")
                break

        PageInsights_5G = Insights_5G_Page(self.driverC)
        log1.info("5G page is loaded successfully")
        get_text1 = PageInsights_5G.Text_5G_InsightsPage().text
        print(get_text1)
        log1.info("The main title headline is -The future is 5G")
        # time.sleep(8)
