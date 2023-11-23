from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def run_test_on_remote_browser():
    # Specify the remote server URL
    remote_url = "http://34.85.201.58:4499"

    # Set up Chrome options
    chrome_options = Options()
    # Add any specific options you want
    # For example, to run headless: chrome_options.add_argument("--headless")

    # Initialize the remote WebDriver with the updated argument
    driver = webdriver.Remote(command_executor=remote_url, options=chrome_options)

    try:
        # Navigate to a website
        driver.get("https://www.gillette.co.in")
        time.sleep(15)  # Waiting for the page to load
        print("Test completed successfully")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    run_test_on_remote_browser()
