from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://10fastfingers.com/typing-test/english")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]").click()
time.sleep(3)
for i in range(1, 396):
    x = driver.find_element_by_xpath(f"/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[{i}]").text
    driver.find_element_by_xpath("/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input").send_keys(x)
    driver.find_element_by_xpath("/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input").send_keys(" ")
    if i % 100 == 0:
        time.sleep(4)
      
