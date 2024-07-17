from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Update this URL to point to your Selenium Grid Hub
SELENIUM_GRID_URL = "http://<your-selenium-grid-hub-url>:4444/wd/hub"

# Set the desired capabilities for the browser
capabilities = DesiredCapabilities.CHROME.copy()

# Initialize the remote WebDriver
driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)

driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()