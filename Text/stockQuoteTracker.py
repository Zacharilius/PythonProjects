"""
stockquoteTracker

This program will print the current stock prices using Google Finance

"""

import urllib
import re

def getStockQuote(symbol):
    base_url = "http://www.google.com/finance?q="
    content = urllib.urlopen(base_url + symbol).read()
    m = re.search('id="ref_18241_l".*?>(.*?)<', content)
    if m:
        quote = m.group(1)
    else:
        quote = 'no quote available for: ' + symbol
    return quote

print getStockQuote("IBM")

