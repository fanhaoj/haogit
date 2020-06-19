from selenium.webdriver.remote.webdriver import WebDriver

from sele_wework.page.basepage import Basepage


class Addmember(Basepage):
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def save_mem(self):
        pass
