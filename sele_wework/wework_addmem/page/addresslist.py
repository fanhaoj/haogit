from selenium.webdriver.remote.webdriver import WebDriver

from sele_wework.page.basepage import Basepage
from sele_wework.wework_addmem.page.addmember import Addmember


class Addresslist(Basepage):
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def search_mem(self):
        pass

    def add_department(self):
        pass

    def add_mem(self):
        return Addmember(self.driver)

    def delete_mem(self):
        pass