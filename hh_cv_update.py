#!/usr/bin/env python3
# Sctipt to auto update all your CVs on hh.ru

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Constants
CSS_SEL = 'button.HH-Resume-Touch-Button'
DELAY = 10

# Authentication details
login = input("Please type your email  ---> ")
password = input("Please type your password ---> ")

# Chrome is a default browser, change to appropriated one
browser = webdriver.Chrome()
browser.get('https://www.hh.ru/account/login')

# Authentication
emailel = browser.find_element_by_css_selector('input[type="email"]')
emailel.send_keys(login)
passel = browser.find_element_by_css_selector('input[type="password"]')
passel.send_keys(password)
passel.submit()

# Looking for CV's links
browser.get('https://hh.ru/applicant/resumes')
links = []
resume_els = browser.find_elements_by_css_selector(\
    'a.b-resumelist-vacancyname')
for r in resume_els:
	links.append(r.get_attribute('href'))

# Update all CVs
for link in links:
    browser.get(link)
    refresh_button = WebDriverWait(browser, DELAY).until(\
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CSS_SEL)))
    try:
        refresh_button[0].click()
    except:
        refresh_button[1].click()

# Quit webdriver
browser.quit()
