from selenium.webdriver.common.by import By

from sele_wework.page.basepage import Basepage
from sele_wework.page.login import Login
from sele_wework.page.rigist import Rigist
from selenium.webdriver.remote.webdriver import WebDriver

class Index(Basepage):
    base_url = 'https://work.weixin.qq.com/'
    def goto_login(self):
        self.driver.find_element(By.XPATH, '//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return Login(self.driver)

    def goto_regist(self):
        self.driver.find_element(By.XPATH, '//*[@id="tmp"]/div[1]/a[2]').click()
        return Rigist(self.driver)