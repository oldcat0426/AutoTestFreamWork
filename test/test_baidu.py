import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')

    # 创建chrome参数对象
    opt = webdriver.ChromeOptions()
    # 把chrome设置成为无界面模式
    opt.set_headless()

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        # executable_path为驱动路径，options为
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe', options=opt)
        self.driver.get(URL)

    def tearDown(self):
        self.driver.quit()

    def test_search0(self):
        self.driver.find_element(*locator_kw).send_keys('selenium')
        self.driver.find_element(*locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*locator_result)
        for link in links:
            print(link.text)

    def test_search1(self):
        self.driver.find_element(*locator_kw).send_keys('python')
        self.driver.find_element(*locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*locator_result)
        for link in links:
            print(link.text)

if __name__ == '__main__':
    unittest.main()






driver.find_element(*locator_kw).send_keys('selenium')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
driver.quit()

