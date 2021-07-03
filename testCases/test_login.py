import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login():
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"




    #baseURL = ReadConfig.getApplicationURL()
    #username = ReadConfig.getUseremail()
    #password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*************************Test_001_Login***************************")
        self.logger.info("********************Verifying Home page Title*********************")
        self.driver=setup
        self.driver.get(self.baseURL)

        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******************Home Page Title Test pass*****************")

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\"+"test_homePageTitle.png")
            #self.driver.save_screeshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****************Home Page Title Test Failed*****************")
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title1=self.driver.title
        if act_title1=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()

        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "test_login.png")
            #self.driver.save_screeshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False




