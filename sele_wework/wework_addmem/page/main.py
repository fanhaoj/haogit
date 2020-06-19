from selenium.webdriver.remote.webdriver import WebDriver

from sele_wework.page.basepage import Basepage
from sele_wework.wework_addmem.page.addresslist import Addresslist


class Main(Basepage):
    base_url='https://work.weixin.qq.com/wework_admin/frame#index'
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def home_page(self):
        pass

    def address_list(self):
        return Addresslist(self.driver)

    def app_manage(self):
        pass

    def per_contact(self):
        pass

    def manage_tool(self):
        pass

    def mycompany(self):
        pass