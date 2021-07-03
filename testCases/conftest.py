from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome("C:/Users/Sanjay/PycharmProjects/nopcommerceApp/driver/chromedriver.exe")
        print("Launching ChromeDriver")
    elif browser=='firefox':
        driver=webdriver.Firefox("C://Users//Sanjay//PycharmProjects//nopcommerceApp//driver//geckodriver.exe")
        print("Launching FirefoxDriver")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#######################Pytest HTML Report##############################


#def pytest_configure(config):
 #   config.metadata['Project Name'] = 'nop Commerce'
 #   config.metadata['Module Name'] = 'Customer'
 #   config.metadata['Tester'] = 'Sanjay'

#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
#    metadata.pop("JAVA_HOME",None)
#    metadata.pop("Plugins",None)