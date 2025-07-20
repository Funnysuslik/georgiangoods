import argparse
from shops.crawlers.es_crawler import ES_Crawler
# from bp_crawler import BP_Craw

KNOWN_SHOPS = [
  'Zoommer',
]

class Scraper:
  def __init__(self, name=None):
    parser = argparse.ArgumentParser(description='Product scraper')
    parser.add_argument('--name', type=str, help='Product name to search for')
    self.args = parser.parse_args()
    
    self.name = name if name is not None else self.args.name
    
    if self.name is None:
      raise ValueError("Product name must be provided either as a parameter or through --name argument")

  def run(self):
    raw_data = self.get_data()
    return self.parse_data(raw_data)

  # get raw data from the shops
  def get_data(self):
    data = {}

    for shop in KNOWN_SHOPS:
      module = __import__(f'shops.crawlers.{shop.lower()}', fromlist=[shop])
      crawler_class = getattr(module, f'{shop}Crawler')
      crawler = crawler_class()  # Create an instance of the crawler
      data[shop] = crawler.get_data(self.name)  # Call get_data on the instance

    return data

# parse raw data, get products
  def parse_data(self, raw_data):
    shop_products = {}
    for shop, data in raw_data.items():
      print(shop)
      module = __import__(f'shops.parsers.{shop.lower()}', fromlist=[shop])
      parser = getattr(module, shop)
      shop_products[shop] = parser(data).products
      
    return shop_products

  # provide products to the API server

  # save products to the database
  def save_products(self, products):
    pass

if __name__ == "__main__":
  scraper = Scraper()
  products = scraper.run()
  
  # Print the collected products in a readable format
  print("\nCollected Products:")
  print("==================")
  for shop, shop_products in products.items():
    print(f"\n{shop}:")
    for product in shop_products:
      print(f"- {product}")