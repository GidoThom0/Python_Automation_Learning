from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

url = 'https://gabrielecirulli.github.io/2048/'

# Set up the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run browser in headless mode
browser = webdriver.Chrome(options=options)

# Open the search page
print(f"Opening page with url: {url}")
browser.get(url)
time.sleep(3)  # Wait for images to load

# Get all links on the page
pageLinks = browser.find_elements(By.XPATH, '//a[@href]')

# Store URLs before navigating
urls = [link.get_attribute("href") for link in pageLinks]

for url in urls:
    try:
        response = requests.get(url)
        print(f"URL: {url}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

print('Done!')
browser.quit()