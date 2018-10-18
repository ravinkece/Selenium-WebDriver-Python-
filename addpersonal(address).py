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
browser.find_element_by_id("ADD").click()
time.sleep(30)
browser.switch_to_default_content()
time.sleep(2)

selectaddresstype = Select(browser.find_element_by_name("inp_addresstype_code"))
selectaddresstype.select_by_value("C")

browser.find_element_by_name("inp_address").send_keys("Jalan Haji Nasir RT 01/RW 05, Tangerang Selatan")

subdis = browser.find_element_by_name("inp_subdistrict_id")
subdis.send_keys("20 Ilir D II")
subdis.send_keys(Keys.TAB)

dis = browser.find_element_by_name("inp_district_id")
dis.send_keys("Bakongan")
dis.send_keys(Keys.TAB)

city = browser.find_element_by_name("inp_city_id")
city.send_keys("Aceh Selatan")
city.send_keys(Keys.TAB)

state = browser.find_element_by_name("inp_state_id")
state.send_keys("Nanggroe Aceh Darussalam")
state.send_keys(Keys.TAB)

country = browser.find_element_by_name("inp_country_id")
country.send_keys("Indonesia")
country.send_keys(Keys.TAB)

browser.find_element_by_name("inp_zipcode_id").send_keys("14121")

browser.find_element_by_name("inp_phone").send_keys("02199915532")

statusown = Select(browser.find_element_by_name("inp_owner_status"))
statusown.select_by_value("OP")

browser.find_element_by_name("inp_address_distance").send_keys("30")

livstat = Select(browser.find_element_by_name("inp_living_status"))
livstat.select_by_value("LWP")

browser.find_element_by_id("btn_a_1").click()

#browser.find_element_by_id("btn_a_0").click() [CANCEL]
