import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\Python27\chromedriver.exe')
browser.get("https://sfid.dataon.com/sf6/")
time.sleep(10)

browser.find_element_by_id("txtAccount").send_keys("dataon")
time.sleep(2)

browser.find_element_by_id("txtUserName").send_keys("gordon")
time.sleep(2)

browser.find_element_by_id("txtPassword").send_keys("password123")
time.sleep(2)

browser.find_element_by_id("btn-logon").click()
time.sleep(10)

browser.find_element_by_xpath("//*[@id=\"menu_3\"]").click()
time.sleep(8)

browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul[2]/li[7]/ul/li[1]/a").click()
time.sleep(8)

browser.switch_to.frame(browser.find_element_by_name("frmSFBody"))
browser.find_element_by_id("cal_periodstart").clear()
browser.find_element_by_id("cal_periodstart").send_keys("01/01/2009")
time.sleep(8)

browser.find_element_by_id("cal_periodend").clear()
browser.find_element_by_id("cal_periodend").send_keys("07/31/2018")
time.sleep(8)

browser.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/div/div/form/div[1]/fieldset[1]/table/tbody/tr/td[2]/input[5]").click()