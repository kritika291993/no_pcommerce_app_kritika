from selenium.webdriver.common.by import By
class loginPage :
    # kind_of_element name_of_element type_of_locator
    input_username_id="Email"
    input_password_id = "Password"
    btn_submit_xpath="//button[normalize-space()='Log in']"
    link_logout_xpath="//a[normalize-space()='Logout']"
    link_logo_id = "//div[@id='ajaxBusy']"

    def __init__(self,driver):
        self.driver= driver

    def setUsername(self,email):
        self.driver.find_element(By.ID, self.input_username_id).clear()
        self.driver.find_element(By.ID, self.input_username_id).send_keys(email)

    def setUpasword(self,password):
        self.driver.find_element(By.ID, self.input_password_id).clear()
        self.driver.find_element(By.ID, self.input_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def clickLogOut(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def verifyLogo(self):
        status = self.driver.find_element(By.XPATH, self.link_logo_id).is_displayed()
        return status



