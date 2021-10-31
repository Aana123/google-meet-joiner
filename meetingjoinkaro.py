import os
import time
from selenium import webdriver

os.environ['PATH'] += r"C:\Users\apoor\Downloads\chromedriver_win32"
driver = webdriver.Chrome()
driver.get("https://meet.google.com/hvy-odeb-oet")

time.sleep(3000)

# search_box = driver.find_element_by_id("i3")
# search_box.send_keys("Meeting Join Karo")
# search_box.submit()
