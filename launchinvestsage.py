from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import selenium

# Provide the path to your chromedriver executable
chromedriver_path = "C://Browserdrivers//chromedriver.exe"

# Set up the service
service = Service(chromedriver_path)

# Set up Chrome options if needed
options = Options()
# Example: You can add arguments to Chrome options if necessary
# options.add_argument("--headless")  # Uncomment to run in headless mode

# Initialize the Chrome driver with service and options
driver = webdriver.Chrome(service=service, options=options)

# Open Google
driver.get("https://www.investsage.com")

# Optional: Wait for a few seconds to see the page
import time
time.sleep(10)

# Close the driver
driver.quit()