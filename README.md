# Boston Apartment Hunting Bot

This project is a Python-based web scraping bot that automates the process of finding affordable apartment listings in Boston from Apartments.com. The bot uses Selenium to navigate the site, extract listing details, filter them based on your criteria, and save the results to a CSV file for easy review.

## Features

- Scrapes apartment listings from Apartments.com for Boston, MA
- Extracts property name, rent, number of bedrooms, and listing URL
- Filters listings by maximum rent and minimum bedrooms (configurable)
- Handles pagination to scrape multiple result pages
- Saves results to `boston_apartments.csv`
- Modular filtering logic for easy customization

## Tech Stack

- Python 3.x
- Selenium
- pandas
- ChromeDriver

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Download [ChromeDriver](https://chromedriver.chromium.org/downloads)** and ensure it matches your Chrome version and is in your PATH.

4. **Configure your search criteria**  
   Edit `config.py` to set your `MAX_RENT` and `MIN_BEDROOMS`.

5. **Create a `.env` file**  
   Copy the `.env.example` or create your own with your email and filter settings (see project instructions).

## Usage

Run the bot with:

```
python main.py
```

The script will scrape listings and save the results to `boston_apartments.csv`.

## Customization

- **Filtering:**  
  Edit `utils/filters.py` to change how listings are filtered.
- **Notifications:**  
  You can extend the script to send email or Discord notifications for new listings.

## Disclaimer

- This project is for educational purposes.
- Please respect Apartments.com's terms of service and robots.txt.

## License

MIT License
