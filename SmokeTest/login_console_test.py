# ! /usr/bin/env python3
# _*_ coding: utf-8

from selenium import webdriver 
from time import sleep

browser = webdriver.Chrome()
browser.get("http://10.0.0.140:8050")

print('设置浏览器打开')

browser.maximize_window()
print('after maximize_window')

sleep(2)

browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/form/div[2]/div/div[1]/input").send_keys("shuo.zhang.x@cloudminds.com")
browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/form/div[3]/div/div[1]/input").send_keys("123456")

browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/form/div[5]/div/div/div/button").click()

sleep(5)
browser.quit()

