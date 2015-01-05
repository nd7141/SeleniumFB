# -- coding: utf-8 --

from fb_credentials import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from devcontrol import *
from selenium.common.exceptions import NoSuchElementException
import time	
import os

def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

 
SLEEP = 2
cities=["People who live in Los Angeles, California","People who live in Chicago, Illinois","People who live in Washington, District of Columbia","People who live in San Francisco, California","People who live in Philadelphia, Pennsylvania","People who live in Boston, Massachusetts","People who live in Houston, Texas","People who live in Miami, Florida","People who live in Detroit, Michigan","People who live in Atlanta, Georgia","People who live in Sydney, Australia","People who live in Phoenix, Arizona","People who live in Melbourne, Victoria, Australia","People who live in Tampa, Florida","People who live in San Diego, California","People who live in Durban, KwaZulu-Natal","People who live in Birmingham, United Kingdom","People who live in Cleveland, Tennessee","People who live in Minneapolis, Minnesota","People who live in Orlando, Florida","People who live in Manchester, United Kingdom","People who live in Liverpool","People who live in Brisbane, Queensland, Australia"]

browser = webdriver.Firefox()
time.sleep(SLEEP)


browser.delete_all_cookies()
time.sleep(SLEEP)
browser.get('http://www.facebook.com')
try:
	element = WebDriverWait(browser, 20).until(
	EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
	)
finally:
	browser.find_element_by_xpath('//*[@id="email"]').send_keys(fb_email)


browser.find_element_by_xpath('//*[@id="pass"]').send_keys(fb_password)
SendKeys("""{ENTER}""")





time.sleep( 3 )
for i in cities:
	if check_exists_by_xpath('//*[@id="u_0_d"]/div[3]')==True:
		browser.find_element_by_xpath('//*[@id="u_0_d"]/div[3]').send_keys("%s"%i)
		SendKeys("""{ENTER}""")
		time.sleep( 3 )
		flag01="off"
		timer01=0
		while flag01=="off":

			if check_exists_by_xpath('//*[@id="browse_end_of_results_footer"]/div/div/div')==True: #Check for the "End of results"
				flag01="on"
				SendKeys("""^s""")
				time.sleep( 2 )
				SendKeys("""{RIGHT}""")
				time.sleep( 2 )
				SendKeys(".html")
				time.sleep( 2 )
				SendKeys("""{ENTER}""")
				time.sleep( 15 )
				browser.quit()
				time.sleep( 2 )
				continue
			else:
				SendKeys("""{END 20}""")
	elif check_exists_by_xpath('//*[@id="u_0_c"]/div[3]')==True:
		browser.find_element_by_xpath('//*[@id="u_0_c"]/div[3]').send_keys("%s"%i)
		SendKeys("""{ENTER}""")
		time.sleep( 3 )
		while flag01=="off":

			if check_exists_by_xpath('//*[@id="browse_end_of_results_footer"]/div/div/div')==True: #Check for the "End of results"
				flag01="on"
				SendKeys("""^s""")
				time.sleep( 2 )
				SendKeys("""{RIGHT}""")
				time.sleep( 2 )
				SendKeys(".html")
				time.sleep( 2 )
				SendKeys("""{ENTER}""")
				time.sleep( 15 )
				browser.quit()
				time.sleep( 2 )
				continue
			else:
				SendKeys("""{END 20}""")
	else:
		flag01="off"
		browser.find_element_by_xpath('//*[@id="u_0_e"]/div[3]').send_keys("%s"%i)
		SendKeys("""{ENTER}""")
		time.sleep( 3 )
		while flag01=="off":

			if check_exists_by_xpath('//*[@id="browse_end_of_results_footer"]/div/div/div')==True: #Check for the "End of results"
				flag01="on"
				SendKeys("""^s""")
				time.sleep( 2 )
				SendKeys("""{RIGHT}""")
				time.sleep( 2 )
				SendKeys(".html")
				time.sleep( 2 )
				SendKeys("""{ENTER}""")
				time.sleep( 15 )
				browser.quit()
				time.sleep( 2 )
				continue
			else:
				SendKeys("""{END 20}""")




