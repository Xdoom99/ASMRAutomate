from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open YouTube
driver.get("https://www.youtube.com")

# Wait for the page to load
time.sleep(2)

# Find the search box and input "ASMR" as the search query
search_box = driver.find_element_by_name("search_query")
search_box.send_keys("ASMR")

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(5)

# Close the browser
driver.quit()
