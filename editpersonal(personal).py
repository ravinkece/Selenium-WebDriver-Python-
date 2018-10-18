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

browser.switch_to.frame(browser.find_element_by_id("framecontent_4"))
browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td/div[1]/div/div[17]/div/table/tbody/tr[1]/td/a").click()
time.sleep(5)

browser.find_element_by_name("inp_first_name").clear()

browser.find_element_by_name("inp_first_name").send_keys("ipinns")

browser.find_element_by_name("inp_middle_name").send_keys("Margareth")

browser.find_element_by_name("inp_last_name")

browser.find_element_by_name("inp_official_name")

browser.find_element_by_name("inp_initial_name").send_keys("Valen")

selectnational = Select(browser.find_element_by_name("inp_nationality_code"))
selectnational.select_by_value("USA")

selectsalut = Select(browser.find_element_by_name("inp_salutation_code"))
selectsalut.select_by_value("MR")

selectedu1 = Select(browser.find_element_by_name("inp_edutitle1"))
selectedu1.select_by_value("DR")

selectedu2 = Select(browser.find_element_by_name("inp_edutitle2"))
selectedu2.select_by_value("ST")

browser.find_element_by_name("inp_identity_no").send_keys("8027389742766")

browser.find_element_by_name("cal_indentity_expdate").send_keys("12/04/2020")

browser.find_element_by_name("inp_birthplace").send_keys("Jakarta Selatan")

browser.find_element_by_name("cal_birthdate").send_keys("12/04/2020")

browser.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()

selectreligion = Select(browser.find_element_by_name("inp_religion_code"))
selectreligion.select_by_value("ISLAM")

selectrace = Select(browser.find_element_by_name("inp_race_code"))
selectrace.select_by_value("AID")

selectdialek = Select(browser.find_element_by_name("inp_dialect_code"))
selectdialek.select_by_value("MAL")

selectmarital = Select(browser.find_element_by_name("inp_maritalstatus"))
selectmarital.select_by_value("0")

browser.find_element_by_name("inp_married_place").send_keys("Bali")

browser.find_element_by_name("cal_married_date").send_keys("13/05/2001")

browser.find_element_by_id("btn_a_1").click()

#browser.find_element_by_id("btn_a_0").click() [DELETE]