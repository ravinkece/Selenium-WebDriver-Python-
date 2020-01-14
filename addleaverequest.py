import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\Python27\chromedriver.exe')
browser.get("https://sfid.dataon.com/sf6/")
time.sleep(10)
time.sleep(4)

browser.find_element_by_id("txtAccount").send_keys("dataon")
time.sleep(2)

browser.find_element_by_id("txtUserName").send_keys("gordon")
time.sleep(2)

browser.find_element_by_id("txtPassword").send_keys("password123")
time.sleep(1)

browser.find_element_by_id("btn-logon").click()
time.sleep(10)

browser.find_element_by_xpath("//*[@id=\"menu_2\"]").click()
time.sleep(4)

browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul[2]/li[4]/ul/li[5]/a").click()
time.sleep(4)

browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul[2]/li[4]/ul/li[5]/ul/li[1]/a").click()
time.sleep(3)

browser.switch_to.frame(browser.find_element_by_name("frmSFBody"))
browser.find_element_by_id("ADD").click()	
time.sleep(7)

browser.switch_to_default_content()
time.sleep(5)


browser.find_element_by_id("inp_refdoc").send_keys("D:\\addnewemployee.xlsx")

