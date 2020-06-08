from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from sele_wework.page.basepage import Basepage
from selenium.webdriver.remote.webdriver import WebDriver

class Rigist(Basepage):
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def regist_true(self):
        # self.driver.find_element(By.ID,"corp_name").send_keys('van')
        self.find(By.ID,"corp_name").send_keys('van')
        self.waitforclick(self.driver,5,"//*[@id='corp_industry']/a")
        # WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@id='corp_industry']/a")))
        self.find(By.XPATH,"//*[@id='corp_industry']/a").click()
        sleep(1)
        self.find(By.XPATH,"//*[@id='corp_industry']/div/table/tbody/tr/td[1]/div[1]/a").click()
        sleep(1)
        self.find(By.XPATH, "//*[@id='corp_industry']/div/table/tbody/tr/td[2]/div[1]/div[2]/a").click()
        sleep(1)
        self.find(By.XPATH,'//*[@id="corp_scale_btn"]/a').click()
        sleep(1)
        self.find(By.XPATH, '//*[@id="corp_scale_btn"]/div/ul/li[2]/a/span[2]').click()
        sleep(1)
        self.driver.quit()
        return True



