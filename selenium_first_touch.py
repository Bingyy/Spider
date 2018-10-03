from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait 

browser = webdriver.Chrome()

try:
	browser.get('https://www.baidu.com')
	_input = browser.find_element_by_id('kw')
	_input.send_keys('Python')
	_input.send_keys(Keys.ENTER)
	wait = WebDriverWait(browser, 10)
	wait.until(EC.presence_of_element_located((By.ID, 'content-left')))
	print(browser.current_url)
	print(browser.get_cookies())
	print(browser.page_source)
finally:
	browser.close()