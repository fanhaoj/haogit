from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/")

    def test_demo(self):
        self.driver.find_element(By.XPATH,'//*[@id="tmp"]/div[1]/a[2]').click()