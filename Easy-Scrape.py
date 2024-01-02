from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import requests
import os

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def close_overlay_by_click(driver, selector):
    try:
        overlay_element = driver.find_element(By.CSS_SELECTOR, selector)
        overlay_element.click()
        print("Overlay closed.")
    except (NoSuchElementException, ElementClickInterceptedException):
        print("No overlay found, or couldn't close it.")
        pass  

def fetch_and_download_images_with_selenium(url):

    driver = webdriver.Chrome()  

    driver.get(url)

    if not os.path.exists('images'):
        os.makedirs('images')

    image_count = 0
    while True:

        time.sleep(3)  

        close_overlay_by_click(driver, ".cookie-banner .close-button-selector")

        image_elements = driver.find_elements(By.CSS_SELECTOR, ".item-card-thumb-container img")
        if not image_elements and image_count > 0:
            break  

        for img in image_elements:
            src = img.get_attribute('src')
            if src:
                filename = os.path.join('images', 'image_' + str(image_count) + '.png')
                download_image(src, filename)
                image_count += 1

        try:

            next_button = driver.find_element(By.CSS_SELECTOR, "#inventory-container > inventory > div > assets-explorer > div > div > div.tab-content.rbx-tab-content > div > div.pager-holder > ul > li.pager-next > button > span")
            driver.execute_script("arguments[0].click();", next_button)
        except NoSuchElementException:
            break  
        except ElementClickInterceptedException:
            print("Next button click intercepted, trying again...")
            time.sleep(2)
            continue

    driver.quit()

inventory_url = 'PASTE_COPIED_URL_HERE'
fetch_and_download_images_with_selenium(inventory_url)
