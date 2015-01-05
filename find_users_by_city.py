# -- coding: utf-8 --

from __future__ import division
# from fb_credentials import fb_email, fb_password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# from SendKeys import SendKeys
from devcontrol import *
import time, os, getpass

SLEEP = 3
SCROLLS = 10000
QUERY = "People who live in Moscow, Russia"
URLQUERY = "https://www.facebook.com/search/str/%s/keywords_users" %QUERY
QUERIES = ["People who live in Chicago, Illinois","People who live in Washington, District of Columbia","People who live in San Francisco, California","People who live in Philadelphia, Pennsylvania","People who live in Boston, Massachusetts","People who live in Houston, Texas","People who live in Miami, Florida","People who live in Detroit, Michigan","People who live in Atlanta, Georgia","People who live in Sydney, Australia","People who live in Phoenix, Arizona","People who live in Melbourne, Victoria, Australia","People who live in Tampa, Florida","People who live in San Diego, California","People who live in Durban, KwaZulu-Natal","People who live in Cleveland, Tennessee","People who live in Minneapolis, Minnesota","People who live in Orlando, Florida","People who live in Manchester, United Kingdom","People who live in Liverpool","People who live in Brisbane, Queensland, Australia"]
# QUERIES = cities=["People who live in Los Angeles, California","People who live in Chicago, Illinois"]
# QUERIES = cities=["People who live in Moscow, Russia","People who live in Boston"]
QUERIES = ["People who live in Boston, Massachusetts"]

fb_email = raw_input("Please, enter your facebook email: ")
fb_password = getpass.getpass("Please, enter your facebook password: ")

def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

browser = webdriver.Firefox()
# after you inserted credentials you have some time to manually configure things
# use this time to download the facebook page in order to
# download the facebook page to configure settings
# for later downloads (folder to download, type of files, etc.)
time.sleep(15)


# browser.delete_all_cookies()
time.sleep(SLEEP)
browser.get('http://www.facebook.com')
# insert facebook credentials
try:
	element = WebDriverWait(browser, 20).until(
	EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
	)
finally:
	browser.find_element_by_xpath('//*[@id="email"]').send_keys(fb_email)
browser.find_element_by_xpath('//*[@id="pass"]').send_keys(fb_password)
press_key()
time.sleep(SLEEP)

for q in QUERIES:
	url_q = "https://www.facebook.com/search/str/%s/keywords_users" %q
	print url_q
	browser.get(url_q)
	time.sleep(SLEEP)

	# scroll down no more than max_time seconds or when we found the last user
	max_time = 1800
	start = time.time()
	elapsed_time = time.time() - start
	while elapsed_time < max_time:
		scrolldown()
		time.sleep(SLEEP)
		if check_exists_by_xpath('//*[@id="browse_end_of_results_footer"]/div/div/div'): #Check for the "End of results"
			break
		elapsed_time = time.time() - start
		print 'No more than %s sec for this query' %(max_time - elapsed_time)

	# save the page under queryname.html
	press_ctrl_plus('KEY_S')
	for letter in q.upper():
		try:
			press_key('KEY_%s' %letter)
		except KeyError:
			continue
	press_key()
	time.sleep(1)

browser.quit()