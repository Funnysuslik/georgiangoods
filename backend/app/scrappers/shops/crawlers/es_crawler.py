import requests

class ES_Crawler:
  DEFAULT_HEADERS = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
      "Accept": "application/json",
      "Accept-Language": "en-EN,en;q=0.9",
      "Connection": "keep-alive",
    }

  def __init__(self):
    self.scrapper = requests.Session()
    self.scrapper.headers.update(self.DEFAULT_HEADERS)

  def get_data(self, url):
    response = self.scrapper.get(url)
    return response.content
  
  def add_headers(self, headers):
    self.scrapper.headers.update(headers)

  def add_cookies(self, cookies):
    self.scrapper.cookies.update(cookies)

  def add_post_body(self, post_body):
    self.scrapper.body.update(post_body)

