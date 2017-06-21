from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("http://10.0.0.140:8050")

print('设置浏览器打开')

browser.maximize_window()
print("after maximize_window")

sleep(2)


browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/form/div[2]/div/div[1]/input").send_keys("shuo.zhang.x@cloudminds.com")
browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/form/div[3]/div/div[1]/input").send_keys("123456")

browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/form/div[5]/div/div/div/button").click()

sleep(4)

browser.find_element_by_xpath("//*[@id=\"root\"]/div[1]/md-content/div[1]/md-toolbar/div/div[2]/div[2]/ac-account/md-menu-bar/md-menu/button").click()
#browser.find_element_by_xpath("//*[@id=\"menu_container_4\"]/md-menu-content/div/div[2]/div[2]/a").click()

#menu = browser.find_element_by_id("menu_container_4")
sleep(1)
browser.find_element_by_class_name("login-out-div").click()


