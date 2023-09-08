from utilities.readConfig import ReadConfig
from utilities.customLogger import Logger
from pageObjects.login import loginPage
from utilities.xlutilites import *


class Test002_Login_TestSuite:
    log = Logger()

    @pytest.mark.regression
    def testCase_001_loginddt(self, setup):
        self.log.info("*********Test Case 001 Login with data driven testing******")
        self.driver = setup
        self.log.info("*********successfully lauched appliaction******")
        self.lp_obj = loginPage(self.driver)
        self.path = "testData/LoginData.xlsx"
        self.sheet_name = "Sheet1"
        n_row = getRowCount(self.path, self.sheet_name)
        n_col = getColoumnCount(self.path, self.sheet_name)
        self.status = []
        for r in range(2, n_row+1):
            self.lp_obj.setUsername(readData(self.path, self.sheet_name, r, 1))
            self.lp_obj.setUPassword(readData(self.path, self.sheet_name, r, 2))
            self.ex_status = readData(self.path, self.sheet_name, r, 3)
            self.log.info("*********Login to application******")
            self.lp_obj.clickLogIn()

            if self.driver.title == "Dashboard / nopCommerce administration":
                if self.ex_status == "Pass":
                    self.lp_obj.clickLogOut()
                    self.status.append("Passed")
                else:
                    self.driver.save_screenshot("./screenShots/testCase_001_loginddt.png")
                    self.status.append("Failed")
            else:
                if self.ex_status == "Fail":
                    self.status.append("Passed")
                else:
                    self.driver.save_screenshot("./screenShots/testCase_001_loginddt.png")
                    self.status.append("Failed")

            print(self.status)

        if "Failed" in self.status:
            self.log.error("testCase_001_loginddt : Failed")
            self.log.info("*********Test Case 001 Login with data driven testing completed ******")
            assert False
        else:
            self.log.info("testCase_001_loginddt : Passed")
            self.log.info("*********Test Case 001 Login with data driven testing completed ******")
            assert True

