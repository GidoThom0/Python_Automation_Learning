from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

imageSearch = 'cars'  # Input what you want to search
numOfImages = 5  # Number of images to download

# Create directory to store images
os.makedirs('images', exist_ok=True)

# Base URL for Imgur search
baseUrl = 'https://imgur.com/search/score?q='
searchUrl = baseUrl + '+'.join(imageSearch.split())

# Set up the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run browser in headless mode
browser = webdriver.Chrome(options=options)

# Open the search page
print(f"Searching for images: {imageSearch}")
browser.get(searchUrl)
time.sleep(3)  # Wait for images to load

# Get the top image posts
posts = browser.find_elements(By.CSS_SELECTOR, '.post a.image-list-link')

if not posts:
    print("No images found.")
else:
    print(f"Found {len(posts)} images. Downloading up to {numOfImages}.")

# Loop through image posts and download images
for i in range(min(numOfImages, len(posts))):
    postUrl = 'https://imgur.com/' + posts[i].get_attribute('href')

    if postUrl:
        browser.get(postUrl)
        time.sleep(3)   # Wait for post to load

        # Get Image Url
        imgUrl = browser.find_element('.imageContainer img').get_attribute('src')
        print(imgUrl)

        # Download and save the image
        print(f"Downloading {imgUrl}...")
        imgData = requests.get(imgUrl).content
        imgName = 'image' + str(i + 1) + '.jpg'

        with open(os.path.join('images', imgName), 'wb') as imgFile:
            imgFile.write(imgData)

# Close the browser
browser.quit()

print("Download complete!")
