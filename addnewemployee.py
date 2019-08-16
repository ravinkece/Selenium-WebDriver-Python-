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
time.sleep(2)

browser.find_element_by_id("txtPassword").send_keys("password123")
time.sleep(2)

browser.find_element_by_id("btn-logon").click()
time.sleep(10)
time.sleep(10)

browser.find_element_by_xpath("//*[@id=\"menu_1\"]").click()
time.sleep(10)

browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul[2]/li[2]/ul/li[1]/a").click()
time.sleep(8)

browser.switch_to.frame(browser.find_element_by_name("frmSFBody"))
browser.find_element_by_id("ADD").click()
time.sleep(15)

browser.switch_to_default_content()

browser.find_element_by_name("inp_first_name").send_keys("Muhammad")

browser.find_element_by_name("inp_middle_name").send_keys("Arivin")

browser.find_element_by_name("inp_last_name").send_keys("Wijaya")

browser.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()

browser.find_element_by_name("inp_identity_no").send_keys("1412503573")

browser.find_element_by_name("inp_birth_place").send_keys("Jakarta")

browser.find_element_by_name("cal_birth_date").send_keys("12/04/1997")

select = Select(browser.find_element_by_name("inp_religion_code"))
select.select_by_value("ISLAM")

selectmarital = Select(browser.find_element_by_name("inp_marital_status"))
selectmarital.select_by_value("1")

selectaddresstype = Select(browser.find_element_by_name("inp_addresstype_code"))
selectaddresstype.select_by_value("B")

browser.find_element_by_name("inp_address").send_keys("Jalan Haji Nasir RT 01/RW 02 Paninggilan Utara, CIledug Tangerang")

kota =browser.find_element_by_name("inp_city_id")
kota.send_keys("Tangerang Selatan")
kota.send_keys(Keys.TAB)
time.sleep(3)

browser.find_element_by_name("inp_zipcode").send_keys("41142")

browser.find_element_by_name("inp_phone").send_keys("0219915532")

browser.find_element_by_name("inp_email").send_keys("ravinkece@gmail.com")

selectempstatus = Select(browser.find_element_by_name("inp_emp_status"))
selectempstatus.select_by_value("PROBATION~Y~N~6")

browser.find_element_by_name("inp_emp_no").send_keys("3123171204970004")

browser.find_element_by_name("cal_join_date").send_keys("07/04/2018")

curpos = browser.find_element_by_name("inp_emp_pos")
curpos.send_keys("Account Manager [SLSTAFF]")
time.sleep(3)
curpos.send_keys(Keys.TAB)

selectjobstatus = Select(browser.find_element_by_name("inp_job_status"))
selectjobstatus.select_by_value("DIRECT")

selectjobgrade = Select(browser.find_element_by_name("inp_job_grade"))
selectjobgrade.select_by_value("2")

selectwl = Select(browser.find_element_by_name("inp_work_location"))
selectwl.select_by_value("BO")

selectcost = Select(browser.find_element_by_name("inp_costcenter"))
selectcost.select_by_value("100")

supervisor = browser.find_element_by_name("inp_supervisor")
supervisor.send_keys("Aashka Valencia, Software Documentation Officer")
time.sleep(3)
supervisor.send_keys(Keys.TAB)

manager = browser.find_element_by_name("inp_manager")
manager.send_keys("Alberta Tyas, Solution Consultant")
time.sleep(7)
manager.send_keys(Keys.TAB)

browser.find_element_by_name("inp_taxfilenumber").send_keys("12131415161718192021222")

browser.find_element_by_name("cal_taxfiledate").send_keys("07/04/2018")

#it should be check "start shift" date same with "join date"

selectshift = Select(browser.find_element_by_name("inp_startshiftorder"))
selectshift.select_by_value("3")

browser.find_elements_by_css_selector("input[type='checkbox'][value='Y']")[0].click()

browser.find_elements_by_css_selector("input[type='radio'][value='OFFICE']")[0].click()

time.sleep(10)
leave = browser.find_element_by_name("inp_leavecode")
#in firefox can, but in chrome can't
time.sleep(10)
leave.send_keys("Annual Leave")
time.sleep(10)
leave2 = browser.find_element_by_name("unselinp_leavecode")
time.sleep(5)
leave2.send_keys(Keys.TAB)
time.sleep(10)
leave2.send_keys(Keys.ENTER)
time.sleep(10)
leave2.send_keys(Keys.TAB)
time.sleep(10)
leave2.send_keys(Keys.ENTER)



selectleave.select_by_value("1").click()
browser.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr[2]/td/div/div/form/div[1]/fieldset[5]/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/input[1]").click()

selectreimburs = Select(browser.find_element_by_name("unselinp_reimcode"))
selectreimburs.select_by_value("EXP")
browser.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr[2]/td/div/div/form/div[1]/fieldset[6]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/input[1]")

#username should be same with first_name + 2018

selectstatusactive = Select(browser.find_element_by_name("inp_user_status"))
selectstatusactive.select_by_value("1")

browser.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()

selectleave = Select(browser.find_element_by_name("unselinp_acsgroup"))
selectleave.select_by_value("23").click()
browser.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr[2]/td/div/div/form/div[1]/fieldset[8]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/input[1]")

browser.find_element_by_id("btn_a_1").click()

#browser.find_element_by_id("btn_a_0").click()  [CANCEL]
