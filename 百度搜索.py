from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id = 'kw']").send_keys("斗罗大陆")
driver.find_element_by_xpath("//*[@id = 'su']").click()
time.sleep(10)
