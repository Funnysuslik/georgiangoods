from shops.crawlers.es_crawler import ES_Crawler

class ZoommerCrawler(ES_Crawler):
  API_URL = 'https://api.zoommer.ge/v1/Products/v3?Page=1&Limit=30&Name='

  def __init__(self):
    super().__init__()

  def get_data(self, name: str):
    return super().get_data(f'{self.API_URL}{name}')

