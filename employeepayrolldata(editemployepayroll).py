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

browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul[2]/li[7]/ul/li[2]/a").click()
time.sleep(8)

browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul[2]/li[7]/ul/li[2]/ul/li[1]/a").click()
time.sleep(8)

browser.switch_to.frame(browser.find_element_by_name("frmSFBody"))
browser.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td/div[1]/div/div[23]/div/table/tbody/tr[1]/td/a").click()
time.sleep(10)

browser.switch_to_default_content()
browser.find_element_by_id("inp_show_paytemplate").click()

selectcur = Select(browser.find_element_by_name("inp_currency_code"))
selectcur.select_by_value("EUR")

gaji = browser.find_element_by_id("inp_basic_salary").clear()
browser.find_element_by_id("inp_basic_salary").send_keys("1000000")

tglgaji = browser.find_element_by_id("cal_basic_effdate").clear()
tglgaji.send_keys("12/04/2019")

ket = browser.find_element_by_id("inp_basic_type").clear()
ket.send_keys("Senior")

formula = browser.find_element_by_id("inp_formula").clear()
formula.send_keys("MONEY")

browser.find_element_by_id("inp_taxed").click()

browser.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()

payfreq = Select(browser.find_element_by_name("inp_payfrequency"))
payfreq.select_by_value("HOUR")

browser.find_element_by_id("inp_taxbornebycomp_dec").clear()
browser.find_element_by_id("inp_taxbornebycomp_dec").send_keys("50000")

browser.find_element_by_id("inp_taxpenaltybornebycomp_dec").clear()
browser.find_element_by_id("inp_taxpenaltybornebycomp_dec").send_keys("10000000

browser.fin