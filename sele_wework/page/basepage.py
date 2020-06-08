from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Basepage():
    base_url=''
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            option=Options()
            option.debugger_address="127.0.0.1:9222"
            self.driver=webdriver.Chrome(options=option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        else:
            self.driver=driver

        if self.base_url != '':
            self.driver.get(self.base_url)

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def waitforclick(self,time,locator):
        return WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@id='corp_industry']/a")))

    def waitforele(self,conditions,time):
        return WebDriverWait(self.driver,5).until(expected_conditions.element((By.XPATH,"//*[@id='corp_industry']/a")))

