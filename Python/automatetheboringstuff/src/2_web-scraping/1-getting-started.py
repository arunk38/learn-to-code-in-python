import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Personal\Softwares\chromedriver_win32\chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.co.in');
time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
