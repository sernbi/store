from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"F:\python自动化\自动化测试\day01\任务\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id = 'accountID']").send_keys("wsz")
driver.find_element_by_xpath("//*[@id = 'passwordID']").send_keys("8888")
driver.find_element_by_xpath("//*[@id = 'areaID']").send_keys("北京市")
driver.find_element_by_xpath("//*[@id = 'sexID2']").click()
driver.find_element_by_xpath("//*[@value = 'spring']").click()
driver.find_element_by_xpath("//*[@value = 'winter']").click()
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"F:\python自动化\自动化测试\day01\picture.jpg")

time.sleep(5)
driver.quit()