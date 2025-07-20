import json
from typing import Any, Callable, List

from bs4 import BeautifulSoup

class BaseParser:
  def __init__(self, raw_data: str):
    self.raw_data = raw_data
    self.preprocess()
    self.products = self.parse()

  def _try_parsers(self, data: str, parsers: List[Callable[[str], Any]]) -> Any:
    """Try multiple parsers in sequence and return the first successful result."""
    for parser in parsers:
      try:
        return parser(data)
      except Exception:
        continue
    raise ValueError("Failed to parse data with any of the provided parsers")

  def preprocess(self):
    self.raw_data = self._try_parsers(
      self.raw_data,
      [json.loads, lambda x: BeautifulSoup(x, 'html.parser')]
    )

  def parse(self):
    pass