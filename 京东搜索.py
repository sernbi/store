from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://search.jd.com//")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id = 'keyword']").send_keys("棉被")
driver.find_element_by_xpath("//*[@class = 'input_submit']").click()
#暂存5秒之后跳转页面
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[2]/div/div[4]/a/em").click()



time.sleep(10)

