from shops.parsers.base import BaseParser

class Zoommer(BaseParser):
  DOMAIN = 'https://zoommer.ge'

  def __init__(self, raw_data):
    super().__init__(raw_data)

  def parse(self):
    products = []
    for product in self.raw_data['products']:
      products.append({
        'name': product['name'],
        'price': product['price'],
        'image': product['imageUrl'],
        'link': f'{self.DOMAIN}/{product["route"]}',
      })
    
    return products

