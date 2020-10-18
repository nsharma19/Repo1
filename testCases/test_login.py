from selenium import webdriver
from utilities.readProperties import Readconfig
from pageObjects.PageObjects import LoginPage
import pytest
from utilities.customLogger import LogGen

class Test_login001:
    logger = LogGen.log()
    base_url = Readconfig.getAppUrl()
    user_name = Readconfig.getAppUsername()
    user_password = Readconfig.getAppUsername()
    def test_loginPageTitle(self):
        self.logger.info("******Launching Application********")
        self.driver = webdriver.Chrome(executable_path="C:/Users/Owner/Desktop/chromedriver/chromedriver.exe")
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******Title passed******")
        else:
            self.driver.save_screenshot(".\\Screen_Shots\\"+"loginpage.png")
            self.logger.info("******Title failed******")
            assert False
    def test_homePage(self):
        self.logger.info("******Home page Title******")
        self.driver = webdriver.Chrome(executable_path="C:/Users/Owner/Desktop/chromedriver/chromedriver.exe")
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.user_name)
        self.lp.enter_password(self.user_password)
        self.lp.click_login()
        act_homePageTitle = self.driver.title
        if act_homePageTitle == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******Homa page Title passed******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screen_Shots\\" + "Homepage.png")
            self.driver.close()
            self.logger.info("******Homa page Title failed******")
            assert False








