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

browser.find_element_by_xpath("//*[@id=\"tab_3\"]").click()
time.sleep(7)

browser.switch_to.frame(browser.find_element_by_id("framecontent_3"))
browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td/div[1]/div/div[17]/div/table/tbody/tr[1]/td/a").click()
time.sleep(10)
browser.switch_to_default_content()

browser.find_element_by_name("inp_address").send_keys("Jalan Haji Nasir RT 01/RW 05, Tangerang Selatan")

subdis = browser.find_element_by_name("inp_subdistrict_id")
subdis.send_keys("Bandar Mataram")
subdis.send_keys(Keys.TAB)

dis = browser.find_element_by_name("inp_district_id")
dis.send_keys("Bandar Mataram")
dis.send_keys(Keys.TAB)

browser.find_element_by_name("inp_zipcode_id")

browser.find_element_by_name("inp_phone").clear()
browser.find_element_by_name("inp_phone").send_keys("02199915532")

statusown = Select(browser.find_element_by_name("inp_owner_status"))
statusown.select_by_value("OP")

browser.find_element_by_name("inp_address_distance").send_keys("30")

livstat = Select(browser.find_element_by_name("inp_living_status"))
livstat.select_by_value("LWP")

#browser.find_element_by_id("btn_a_1").click() [DELETE]

browser.find_element_by_id("btn_a_2").click()

#browser.find_element_by_id("btn_a_0").click() [CANCEL]

browser.switch_to.alert.accept()
