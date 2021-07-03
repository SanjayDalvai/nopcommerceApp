import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login():
    baseURL = "https://admin-demo.nopcommerce.com/"
    path=".//TestData/LoginData.xlsx"


    #username = "admin@yourstore.com"
    #password = "admin"




    #baseURL = ReadConfig.getApplicationURL()
    #username = ReadConfig.getUseremail()
    #password = ReadConfig.getPassword()

    logger=LogGen.loggen()



    def test_login_ddt(self,setup):
        self.logger.info("***************Test_002_DDT_Login********************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel:",self.rows)




        lst_status=[]


        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)



            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"


            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("Test Pass")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Test Failed")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****Failed****")
                    lst_status.append("Fail")



                elif self.exp == 'Fail':
                    self.logger.info("Test Pass")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT Testcase Pass....")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Testcase Failed...")
            self.driver.close()
            assert False




















