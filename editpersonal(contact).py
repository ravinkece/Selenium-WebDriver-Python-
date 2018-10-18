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

browser.find_element_by_xpath("//*[@id=\"menu_1\"]").click()
time.sleep(4)

browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul[2]/li[2]/ul/li[1]/a").click()
time.sleep(8)

browser.switch_to.frame(browser.find_element_by_name("frmSFBody"))
browser.find_element_by_id("ach_cdata_ardata_1_2_0").click()
time.sleep(7)

browser.find_element_by_xpath("/html/body/div[5]/div[2]/table/tbody/tr/td[2]/img[1]").click()
time.sleep(10)

browser.switch_to_default_content()
time.sleep(5)

browser.find_element_by_xpath("//*[@id=\"tab_2\"]").click()
time.sleep(7)

browser.switch_to.frame(browser.find_element_by_id("framecontent_2"))
time.sleep(3)

browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td/div[1]/div/div[15]/div/table/tbody/tr[1]/td/a").click()
time.sleep(5)

browser.find_element_by_name("inp_phone")

browser.find_element_by_name("inp_phone_ext").send_keys("021")

browser.find_element_by_name("inp_email")

browser.find_element_by_id("btn_a_0").click()

time.sleep(10)

browser.switch_to.alert.accept()