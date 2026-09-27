# Competitor Price Tracker

-> A Python web scraping project that extracts product information across multiple pages and saves the collected data to a CSV file.

## Features:

- Extracts product names
- Extracts prices and currencies
- Extracts product availability
- Extracts product URLs
- Handles pagination automatically
- Saves the collected data to a CSV file

## Technologies used:

- Python
- Requests
- Selectolax
- Pandas

## Data source:

This project uses the web scraper test site:

https://webscraper.io/test-sites/pagination

The site is used as a practice/demo source for building and testing the scraper

## Pagination

The scraper uses the site's 'next' link to move from one page to the next. It continues collecting products until there are no more pages.

## Output

The scraper collects the extracted product data into a Pandas DataFrame and saves it as: 

'products.csv'

The CSV contains the following fields:

- Product Name
- Price
- Currency
- Availability
- Product URL

## How to run

1. Clone the repository:

In terminal:

'''bash
git clone https://github.com/Donia-Yaser/competitor-price-tracker.git

2. Navigate into the project directory:

'''bash
cd competitor-price-tracker

3. Install the required dependencies:

'''bash
pip install -r requirements.txt

4. Run the scraper

'''bash
python scraper.py

5. The scraped data will be saved as:

'''bash
products.csv