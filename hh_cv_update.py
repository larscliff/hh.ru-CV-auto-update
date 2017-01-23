#!/usr/bin/env python3

from selenium import webdriver

# authentication details
LOGIN = input("Please type your email  ---> ")
PASSWORD = input("Please type your password ---> ")

# chrome is default browser, change to appropriated one
browser = webdriver.Chrome()
browser.get('https://www.hh.ru/account/login')

# authentication
emailel = browser.find_element_by_css_selector('input[type="email"]')
emailel.send_keys(LOGIN)
passel = browser.find_element_by_css_selector('input[type="password"]')
passel.send_keys(PASSWORD)
passel.submit()

# parse links of all CVs
browser.get('https://hh.ru/applicant/resumes')
links = []
resume_els = browser.find_elements_by_css_selector('a.b-resumelist-vacancyname')
for r in resume_els:
	links.append(r.get_attribute('href'))

# update all CVs
for link in links:
    browser.get(link)
    refresh_button = browser.find_element_by_css_selector('button.HH-\
Resume-Touch-Button')
    refresh_button.click()
    
# quit webdriver
browser.quit()
