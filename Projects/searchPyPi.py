#! python3
# searchPyPi.py  - Opens several search results.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

# Start the browser
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Set path to chromedriver if not in PATH
driver = webdriver.Chrome(options=options)

# Build PyPI search URL
search_query = "+".join(sys.argv[1:])
url = f"https://pypi.org/search/?q={search_query}"

# Open PyPI search page
driver.get(url)
time.sleep(2)  # Wait for page to load

# Get package links
packages = driver.find_elements(By.CSS_SELECTOR, "a.package-snippet")

# Open top results
numOpen = min(5, len(packages))
if numOpen == 0:
    print("No results found or PyPI blocked the request.")
else:
    for i in range(numOpen):
        package_url = packages[i].get_attribute("href")
        print("Opening", package_url)
        driver.execute_script(f"window.open('{package_url}', '_blank');")

# ✅ Keep the browser open
print("Browser will remain open. Press CTRL+C to exit.")
while True:
    time.sleep(1)  # Keeps the script running infinitely
