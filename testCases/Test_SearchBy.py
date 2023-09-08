import pytest
from utilities.readConfig import ReadConfig
from utilities.customLogger import Logger
from pageObjects.login import loginPage
from pageObjects.addCustomer import add_customers
from pageObjects.CustomerSearch import customerInfo


class Test004_Add_Customer_TestSuite:
    log = Logger()

    @pytest.mark.regression
    @pytest.mark.sanity
    def testCase_001_searchcustomer_byemail(self, setup):
        self.log.info("*********Test Case 001 search Customer by Email******")
        self.driver = setup
        self.log.info("*********successfully lauched application******")
        self.lp_obj = loginPage(self.driver)
        self.lp_obj.setUsername(ReadConfig.getUserEmail())
        self.lp_obj.setUPassword(ReadConfig.getUserPassword())
        self.log.info("*********Login to application******")
        self.lp_obj.clickLogIn()
        self.log.info("*********Successfully Login to application******")

        self.ac_obj = add_customers(self.driver)
        self.ac_obj.clickCustomerMainMenu()
        self.ac_obj.clickCustomerLink()

        self.search_obj = customerInfo(self.driver)
        self.search_obj.SearchbyEmail("arthur_holmes@nopCommerce.com")

        self.log.info("*********Searching for Customer By Email******")
        self.status = self.search_obj.verifyEmail("arthur_holmes@nopCommerce.com")
        print(self.status)
        if self.status == True:
            print("testCase_001_searchcustomer_byemail : Passed")
            self.log.info("Test Case 001 search Customer by Email : Passed")
            self.log.info("*********Test Case 001 search Customer by Email completed ******")
            assert True
        else:
            print("testCase_001_searchcustomer_byemail : Failed")
            self.driver.save_screenshot("./screenShots/testCase_001_searchcustomer_byemail.png")
            self.log.error("Test Case 001 search Customer by Email : Failed")
            self.log.error("*********Test Case 001 search Customer by Email completed ******")
            assert False

    @pytest.mark.sanity
    def testCase_002_searchcustomer_byfirstname(self, setup):
        self.log.info("*********Test Case 002 search Customer by First name******")
        self.driver = setup
        self.log.info("*********successfully lauched application******")
        self.lp_obj = loginPage(self.driver)
        self.lp_obj.setUsername(ReadConfig.getUserEmail())
        self.lp_obj.setUPassword(ReadConfig.getUserPassword())
        self.log.info("*********Login to application******")
        self.lp_obj.clickLogIn()
        self.log.info("*********Successfully Login to application******")

        self.ac_obj = add_customers(self.driver)
        self.ac_obj.clickCustomerMainMenu()
        self.ac_obj.clickCustomerLink()

        self.search_obj = customerInfo(self.driver)
        self.search_obj.SearchbyFirstname("James")

        self.log.info("*********Searching for Customer By First name******")
        self.status = self.search_obj.verifyName("James")
        print(self.status)
        if self.status == True:
            print("testCase_002_searchcustomer_byfirstname : Passed")
            self.log.info("Test Case 001 search Customer by First name : Passed")
            self.log.info("*********Test Case 002 search Customer by First name completed ******")
            assert True
        else:
            print("testCase_002_searchcustomer_byfirstname : Failed")
            self.driver.save_screenshot("./screenShots/testCase_002_searchcustomer_byfirstname.png")
            self.log.error("Test Case 001 search Customer by First name : Failed")
            self.log.error("*********Test Case 002 search Customer by First name completed ******")
            assert False

    @pytest.mark.sanity
    def testCase_003_searchcustomer_bylastname(self, setup):
        self.log.info("*********Test Case 003 search Customer by Last name******")
        self.driver = setup
        self.log.info("*********successfully lauched application******")
        self.lp_obj = loginPage(self.driver)
        self.lp_obj.setUsername(ReadConfig.getUserEmail())
        self.lp_obj.setUPassword(ReadConfig.getUserPassword())
        self.log.info("*********Login to application******")
        self.lp_obj.clickLogIn()
        self.log.info("*********Successfully Login to application******")

        self.ac_obj = add_customers(self.driver)
        self.ac_obj.clickCustomerMainMenu()
        self.ac_obj.clickCustomerLink()

        self.search_obj = customerInfo(self.driver)
        self.search_obj.SearchbyLastname("Gates")

        self.log.info("*********Searching for Customer By Last name******")
        self.status = self.search_obj.verifyName("Gates")
        print(self.status)
        if self.status == True:
            print("testCase_003_searchcustomer_bylastname : Passed")
            self.log.info("Test Case 003 search Customer by Last name : Passed")
            self.log.info("*********Test Case 003 search Customer by Last name completed ******")
            assert True
        else:
            print("testCase_003_searchcustomer_bylastname : Failed")
            self.driver.save_screenshot("./screenShots/testCase_003_searchcustomer_bylastname.png")
            self.log.error("Test Case 003 search Customer by Last name : Failed")
            self.log.error("*********Test Case 003 search Customer by Last name completed ******")
            assert False