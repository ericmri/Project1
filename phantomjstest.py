# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import lxml
from selenium.webdriver.support.wait import WebDriverWait

def nextpage(page):
    page.find_element_by_xpath('//a[class="ui-page-next"]')



driver = webdriver.PhantomJS(executable_path="/Users/Eric.xu/phantomjs-2.1.1-macosx/bin/phantomjs")
driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
login_tab = driver.find_element_by_xpath('//*[@class="login-tab login-tab-r"]')
ActionChains(driver).click(login_tab).perform()
time.sleep(1)
username = driver.find_element_by_xpath('//input[@id="loginname"]')
username.send_keys("ericmri")
passw = driver.find_element_by_xpath('//*[@id="nloginpwd"]')
passw.send_keys("qazwsx123321")
b_submit = driver.find_element_by_xpath('//*[@id="loginsubmit"]')
ActionChains(driver).click(b_submit).perform()
time.sleep(3)
driver.save_screenshot('1.png')
driver.find_element_by_xpath('//*[@id="shortcut"]/div/ul[2]/li[7]/div/a').click()
time.sleep(3)
handlers = driver.window_handles
driver.switch_to.window(handlers[1])
driver.save_screenshot('2.png')
b_checkin = driver.find_element_by_xpath('//*[@id="checkinBtn"]')
b_checkin.click()
#print driver.page_source
driver.get('https://a.jd.com/coupons.html')
c_links = driver.find_elements_by_xpath('//a[@class="get-coupon"]/span')
for c_link in c_links:
    if c_link.text == '立即领取':
        c_link.click()
        time.sleep(6)



driver.close()