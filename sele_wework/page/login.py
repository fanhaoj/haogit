from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from sele_wework.page.basepage import Basepage
from sele_wework.page.rigist import Rigist


class Login(Basepage):
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def scanf(self):
        pass

    def goto_regist(self):
        self.driver.find_element(By.CLASS_NAME,'login_registerBar_link').click()
        return Rigist(self.driver)