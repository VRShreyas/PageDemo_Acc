import time
import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage import HomePage
from PageObjects.Page_Insights import Insights_5G_Page
from Utilities.BaseClass import BaseClass


class Test_5GPage(BaseClass):

    def test_page_5G(self):
        HomePage1 = HomePage(self.driverC)  # create object wrt HomePage,
        HomePage1.InsightOption_CLick().click()  # Click on the Insights option
        time.sleep(4)
        # 2.Select the locator for Insights in page.
        InsightFeatures_List = HomePage1.InsightFeature_List()
        for eachInsightFeatureList in InsightFeatures_List:
            InsightFeatureName = eachInsightFeatureList.find_element(By.XPATH, 'li/a').text
            if InsightFeatureName == "5G":
                eachInsightFeatureList.find_element(By.XPATH, 'li[1]/a').click()
                break

        PageInsights_5G = Insights_5G_Page(self.driverC)
        get_text1 = PageInsights_5G.Text_5G_InsightsPage().text
        #time.sleep(8)
        print(get_text1)

        # Assert get_text1 == "The future is 5G" text
