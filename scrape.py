import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website_url):
    print("Launching Chrome Browser!!")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=Service(chrome_driver_path),
        options=options
    )

    try:
        driver.get(website_url) #opens URL
        print("Website loaded....!!")
        time.sleep(5)
        html = driver.page_source   #return HTML content, can be used later for parsing or saving

        return html
    finally:
        time.sleep(5)
        driver.quit()   #close browser
