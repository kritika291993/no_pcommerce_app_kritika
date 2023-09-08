import pytest
import time


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from utilities.readConfig import ReadConfig
# from selenium.webdriver.chrome.service import Service
from pageObjects.login import loginPage
from utilities.customLogger import Logger

from pageObjects.login import loginPage

class Test001_Login_TestSuite:
     log = Logger()

     #BaseURL="https://admin-demo.nopcommerce.com/admin/"

     @pytest.mark.sanity
     def testCase_001_login(self,setup):
          # self.service_obj = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
          # self.driver = webdriver.Edge(service=self.service_obj)
          # # self.servie_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
          # # self.driver = webdriver.Chrome(service=self.servie_obj)
          # self.driver.get(self.BaseURL)
          # self.driver.maximize_window()
          self.log.info("*************Test Case 001 Login****************")
          self.driver=setup
          self.log.info("*************Successfully Launched Application****************")
          self.lp_obj = loginPage(self.driver)
          #self.lp_obj.setUsername("admin@yourstore.com")
          self.lp_obj.setUsername(ReadConfig.getUserEmail())
          #self.lp_obj.setUpasword("admin")
          self.lp_obj.setUpasword(ReadConfig.getUserPassword())
          self.lp_obj.clickLogin()
          self.log.info("*************Login to the applicatiom****************")
          if self.driver.title == "Dashboard / nopCommerce administration":
               print("Passed")
               self.log.info("Test Case 001 Login : Passed")
               assert True
               self.log.info("************Test Case 001 Completely Successfully**************")
               self.lp_obj.clickLogOut()
               self.driver.close()

          else:
               print("Failed")
               self.driver.save_screenshot("./screenShots/testCase001_login.png")
               self.log.error("Test Case 001 Login : Failed")
               assert False
               self.driver.close()

     @pytest.mark.sanity
     def testCase_002_appLogo(self, setup):
          self.log.info("*********Test Case 002 application Logo******")
          self.driver = setup
          self.log.info("*********successfully lauched appliaction******")
          self.lp_obj = loginPage(self.driver)
          self.lp_obj.setUsername(ReadConfig.getUserEmail())
          self.lp_obj.setUpasword(ReadConfig.getUserPassword())
          self.log.info("*********Login to application******")
          self.lp_obj.clickLogin()
          self.log.info("*********Verify application Logo******")
          self.status = self.lp_obj.verifyLogo()
          print(self.status)
          if self.status == True:
               print("testCase_002_appLogo : Passed")
               self.log.info("Test Case 002 Application Logo : Passed")
               self.log.info("*********Test Case 002 Application Logo completed ******")
               self.driver.close()
               assert True
          else:
               print("testCase_002_appLogo : Failed")
               self.driver.save_screenshot("./screenShots/testCase_002_appLogo.png")
               self.log.error("Test Case 002 Application Logo : Failed")
               self.log.error("*********Test Case 002 Application Logo completed ******")
               self.driver.close()
               assert False
