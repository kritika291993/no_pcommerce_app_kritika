import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.firefox.service import Service
from utilities.readConfig import ReadConfig



@pytest.fixture()
def setup(browser):
    BaseURL = ReadConfig.getApplicationURL()
    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser=="edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser=="firefox":
        from selenium.webdriver.firefox.service import Service
        service_obj = Service(r"C:\Drivers\geckodriver-v0.33.0-win32\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get(BaseURL)
    driver.maximize_window()
    yield driver
    driver.quit()


###To get command line input###
def pytest_addoption(parser):  # this will get the values from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value to setup method
    #print(request.config.getoption("--browser"))
    return request.config.getoption("--browser")
