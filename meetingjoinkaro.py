import os
from selenium import webdriver

os.environ['PATH'] += r"C:\Users\apoor\Downloads\chromedriver_win32"
driver = webdriver.Chrome()
driver.get("https://www.duckduckgo.com/")

search_box = driver.find_element_by_id("search_form_input_homepage")
search_box.send_keys("Meeting Join Karo")
search_box.submit()
