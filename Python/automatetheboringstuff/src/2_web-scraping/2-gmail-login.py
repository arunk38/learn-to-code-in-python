import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Personal\Softwares\chromedriver_win32\chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://accounts.google.com/');
time.sleep(1) # Let the user actually see something!
email_id = driver.find_element_by_name('Email')
email_id.send_keys('karun.2210')
email_id.submit()

pwd = driver.find_element_by_id('Password')
pwd.send_keys('foolproof')
pwd.submit()
time.sleep(15) # Let the user actually see something!
driver.quit()