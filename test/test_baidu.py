import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.baidu.com"
base_path = os.path.dirname(os.path.abspath(__file__)) + "\.."
driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')

#创建chrome参数对象
opt = webdriver.ChromeOptions()
#把chrome设置成为无界面模式
opt.set_headless()

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

#executable_path为驱动路径，options为
driver = webdriver.Chrome(executable_path= driver_path, options= opt)
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
print(driver.page_source)
driver.quit()

