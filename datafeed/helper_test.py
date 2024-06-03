import unittest
from io import StringIO
import sys
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2))

  def test_getRatio_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
       stock, bid, ask, price = getDataPoint(quote)
       prices[stock] = price
    self.assertEqual(getRatio(prices["ABC"], prices["DEF"]), prices["ABC"] / prices["DEF"])

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2))

  
  def test_getRatio_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
       stock, bid, ask, price = getDataPoint(quote)
       prices[stock] = price
    self.assertEqual(getRatio(prices["ABC"], prices["DEF"]), prices["ABC"] / prices["DEF"])


  def test_getDataPoint_calculatePriceBidSmallerThanAsk(self):
    quotes = [
      {'top_ask': {'price': 126.24, 'size': 14}, 'timestamp': '2020-09-28 21:44:42.442398', 'top_bid': {'price': 126.11, 'size': 10}, 'id': '0.03377870222101775', 'stock': 'ABC'},
      {'top_ask': {'price': 123.67, 'size': 12}, 'timestamp': '2020-09-28 21:44:42.442398', 'top_bid': {'price': 122.45, 'size': 207}, 'id': '0.03377870222101775', 'stock': 'DEF'}
    ]
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2))

  def test_getRatio_calculatePriceBidSmallerThanAsk(self):
    quotes = [
      {'top_ask': {'price': 126.24, 'size': 14}, 'timestamp': '2020-09-28 21:44:42.442398', 'top_bid': {'price': 126.11, 'size': 10}, 'id': '0.03377870222101775', 'stock': 'ABC'},
      {'top_ask': {'price': 123.67, 'size': 12}, 'timestamp': '2020-09-28 21:44:42.442398', 'top_bid': {'price': 122.45, 'size': 207}, 'id': '0.03377870222101775', 'stock': 'DEF'}
    ]
    prices = {}
    for quote in quotes:
       stock, bid, ask, price = getDataPoint(quote)
       prices[stock] = price
    self.assertEqual(getRatio(prices["ABC"], prices["DEF"]), prices["ABC"] / prices["DEF"])

  def test_getRatio_calculatePriceEqualsToZero(self):
    quotes = [
      {'top_ask': {'price': 126.24, 'size': 14}, 'timestamp': '2020-09-28 21:44:42.442398', 'top_bid': {'price': 126.11, 'size': 10}, 'id': '0.03377870222101775', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 12}, 'timestamp': '2020-09-28 21:44:42.442398', 'top_bid': {'price': 0, 'size': 207}, 'id': '0.03377870222101775', 'stock': 'DEF'}
    ]
    capturedOutput = StringIO() # Create StringIO object
    sys.stdout = capturedOutput # and redirect stdout.
    prices = {}
    for quote in quotes:
       stock, bid, ask, price = getDataPoint(quote)
       prices[stock] = price
    getRatio(prices["ABC"], prices["DEF"])
    sys.stdout = sys.__stdout__ # Reset redirect.
    self.assertEqual("the stock price is 0. Can't calculate the ratio.\n", capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()
