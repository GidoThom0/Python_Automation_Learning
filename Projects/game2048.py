from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://gabrielecirulli.github.io/2048/'

# Set up the WebDriver
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)

# Open the search page
print("Opening game: 2048...")
browser.get(url)
time.sleep(3)  # Wait for images to load

# Get the HTML element to send key presses
htmlElem = browser.find_element(By.TAG_NAME, 'html')

# Move sequence
moves = [Keys.ARROW_LEFT, Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN]
moveCounter = 0

while True:
    try:
        # Check that game is not over
        gameOver = browser.find_element(By.XPATH, "//div[text()='Game Over']")
        
        if gameOver.is_displayed():
            print('Game Over')

            # Extract score message (if available)
            try:
                score_message = browser.find_element(By.XPATH, "//div[contains(@class, 'short:text-sm')]").text
                print(score_message)
            except:
                print("Could not find score message.")

            break
    except:
        pass # Continue playing

    # Perform a move
    htmlElem.send_keys(moves[moveCounter % 4])
    moveCounter += 1

    # Small delay to mimic human play
    time.sleep(0.2)

# Close the browser
browser.quit()

