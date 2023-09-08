import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class add_customers:
    lnk_customer_menu_xpath = "//ul[@role='menu']/li[4]/a/p"
    lnk_customer_xpath = "//ul[@role='menu']/li[4]/ul/li[1]/a/p"
    lnk_addcustomer_xpath = "//a[@class='btn btn-primary']"
    text_customer_id = "Email"
    text_password_id = "Password"
    text_firstname_id = "FirstName"
    text_lastname_id = "LastName"
    rbtn_male_id = "Gender_Male"
    rbtn_female_id = "Gender_Female"
    text_dob_id = "DateOfBirth"
    text_company_id = "Company"
    cbox_taxexempt_xpath = "//input[@id='IsTaxExempt']"

    lst_newsletter_xpath = "//input[@aria-describedby='SelectedNewsletterSubscriptionStoreIds_taglist']"
    lstitem_newletter1_xpath = "//li[contains(text(),'Your store name')]"
    lstitem_newletter2_xpath = "//li[contains(text(),'Test store 2')]"

    lst_customerrole_xpath = "//input[@aria-describedby='SelectedCustomerRoleIds_taglist']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstDefaultRegistered_xpath = "//li/span[text()='Registered']"
    lstitemDeleteRegistered_xpath = "//li/span[text()='Registered']/following-sibling::span"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemModerator_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drp_vendorid_id = "VendorId"
    text_admin_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"
    alert_success_xpath = '//div[@class="alert alert-success alert-dismissable"]'

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerMainMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_xpath).click()

    def clickCustomerLink(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_xpath).click()

    def addNewCustomer(self):
        self.driver.find_element(By.XPATH, self.lnk_addcustomer_xpath).click()

    def setCustomerEmail(self, email):
        self.driver.find_element(By.ID, self.text_customer_id).send_keys(email)

    def setCustomerPassword(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def setCustomerFirstName(self, firstname):
        self.driver.find_element(By.ID, self.text_firstname_id).send_keys(firstname)

    def setCustomerLastName(self, lastname):
        self.driver.find_element(By.ID, self.text_lastname_id).send_keys(lastname)

    def clickCustomerGender(self, gender):
        if gender == "male":
            self.driver.find_element(By.ID, self.rbtn_male_id).click()
        elif gender == "female":
            self.driver.find_element(By.ID, self.rbtn_female_id).click()

    def setCustomerDOB(self, dob):
        self.driver.find_element(By.ID, self.text_dob_id).send_keys(dob)

    def setCustomerCompany(self, company):
        self.driver.find_element(By.ID, self.text_company_id).send_keys(company)

    def clickTaxExemption(self, exempt):
        if exempt=="yes":
            self.driver.find_element(By.XPATH, self.cbox_taxexempt_xpath).click()

    def selectNewsLetter(self, newsletter):
        if newsletter == "Your store name":
            self.driver.find_element(By.XPATH, self.lst_newsletter_xpath).click()
            self.driver.find_element(By.XPATH, self.lstitem_newletter1_xpath).click()
        elif newsletter == "Test store 2":
            self.driver.find_element(By.XPATH, self.lst_newsletter_xpath).click()
            self.driver.find_element(By.XPATH, self.lstitem_newletter2_xpath).click()

    def selectCustomerRole(self, role):
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.lstitemDeleteRegistered_xpath).click()
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == "Registered":
            if not self.driver.find_element(By.XPATH, self.lstDefaultRegistered_xpath).is_displayed():
                self.listItem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        elif role == "Moderators":
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemModerator_xpath)
        else:
            self.listItem = self.driver.find_element(By.XPATH, self.lstitemModerator_xpath)
        time.sleep(5)
        #self.listItem.click()
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def selectVendorManager(self, vendor):
        drpdown_elem = self.driver.find_element(By.ID, self.drp_vendorid_id)
        drpdown = Select(drpdown_elem)
        if vendor=="Vendor1":
            drpdown.select_by_visible_text("Vendor 1")
        elif vendor == "Vendor2":
            drpdown.select_by_visible_text("Vendor 2")

    def setAdminComment(self):
        msg = "this is admin message"
        self.driver.find_element(By.ID, self.text_admin_id).send_keys(msg)

    def clickSaveButton(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def verifySucessAlert(self):
        return self.driver.find_element(By.XPATH, self.alert_success_xpath).text