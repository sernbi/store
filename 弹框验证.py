from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"F:\python自动化\自动化测试\day01\任务\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id = 'alert']").click()
time.sleep(2)
driver.switch_to.alert.accept()




