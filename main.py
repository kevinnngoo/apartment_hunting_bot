from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import random
import logging
import os
from notifications.email_notify import send_email

from config import MAX_RENT, MIN_BEDROOMS, EMAIL_TO, EMAIL_FROM, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS
from utils.filters import is_listing_valid

# Ensure the data folder exists
os.makedirs("data", exist_ok=True)

# Set up logging
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

logging.info("Apartment scraper started.")

# Configure Chrome
options = Options()
options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=options)

# Store filtered listings
results = []

try:
    # Step 1: Open the search results page
    driver.get("https://www.apartments.com/boston-ma/")
    time.sleep(3)

    while True:
        # Step 2: Get all property links from the current page
        property_cards = driver.find_elements(By.CSS_SELECTOR, "a.property-link")
        property_links = [card.get_attribute("href") for card in property_cards if card.get_attribute("href")]

        # Step 3: Visit each property and extract data
        for link in property_links:
            driver.get(link)
            time.sleep(random.uniform(2, 4))  # Avoid bot detection

            try:
                name = driver.find_element(By.ID, "propertyName").text
            except NoSuchElementException:
                name = "N/A"

            try:
                rent = driver.find_elements(By.CLASS_NAME, "rentInfoDetail")[0].text
            except (NoSuchElementException, IndexError):
                rent = "N/A"

            try:
                beds = driver.find_elements(By.CLASS_NAME, "rentInfoDetail")[1].text
            except (NoSuchElementException, IndexError):
                beds = "N/A"

            if not is_listing_valid(rent, beds, MAX_RENT, MIN_BEDROOMS):
                logging.info(f"Skipping {name} | Rent: {rent} | Beds: {beds}")
                continue

            results.append({
                "Name": name,
                "Rent": rent,
                "Beds": beds,
                "URL": link
            })

            logging.info(f"Accepted: {name} | Rent: {rent} | Beds: {beds} | URL: {link}")

        # Step 4: Try to go to next page
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a.next")
            next_button.click()
            time.sleep(3)
        except NoSuchElementException:
            logging.info("No more pages. Exiting pagination loop.")
            break

finally:
    # Step 5: Save results no matter what
    df = pd.DataFrame(results)
    df.to_csv("data/boston_apartments.csv", index=False)
    logging.info(f"Scraping finished. {len(results)} listings saved to data/boston_apartments.csv.")
    driver.quit()
    print("Scraper stopped. Results saved.")

    # Step 6: Print final CSV summary
    df_check = pd.read_csv("data/boston_apartments.csv")
    print(f"✅ Total listings in CSV: {len(df_check)}")
    print(df_check.head())

    # Step 7: Send email notification if results found
    if len(results) > 0:
        subject = "Boston Apartment Bot: New Listings Found"
        body = f"{len(results)} new listings found. See your CSV for details."
        try:
            send_email(
                subject=subject,
                body=body,
                to=EMAIL_TO,
                from_addr=EMAIL_FROM,
                smtp_server=SMTP_SERVER,
                smtp_port=SMTP_PORT,
                smtp_user=SMTP_USER,
                smtp_pass=SMTP_PASS
            )
            print("✅ Email notification sent!")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
