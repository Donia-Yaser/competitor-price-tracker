import requests
from selectolax.parser import HTMLParser
import re
import pandas as pd

url = 'https://webscraper.io/test-sites/pagination'
products = []

while True:

    response = requests.get(url)
    tree = HTMLParser(response.text)
    


    products_nodes = tree.css('div.row.test-items-container.g-4.mb-3 > div.col-md-4.col-xl-4.col-lg-4')

    for product_node in products_nodes:
        product_name = product_node.css_first('div.card-body > h3.card-title.mt-3.mb-0')
        price = product_node.css_first('div.card-footer.row.align-items-center > p.price.col-6.mb-0.text-end.p-0 > span')
        currency = product_node.css_first('div.card-footer.row.align-items-center > p.price.col-6.mb-0.text-end.p-0 > meta')
        product_url = product_node.css_first('div.card-head > a.card-head-url')
        availability = product_node.css_first('div.card-head > div.availability > div.badge')

        product = {
            'Product Name': product_name.attributes.get('title') if product_name is not None else None,
            'Price': int(re.sub(r'[^0-9]', '', price.text())) if price is not None else None,
            'Currency': currency.attributes.get('content') if currency is not None else None,
            'Availability': availability.text().strip() if availability is not None else None,
            'Product URL': product_url.attributes.get('href') if product_url is not None else None
        }
        products.append(product)

    next_page = tree.css_first('a.page-link.next')

    if next_page:
        url = next_page.attributes.get('href')

    else:
        break


df = pd.DataFrame(products)
df.to_csv('products.csv', index=False)