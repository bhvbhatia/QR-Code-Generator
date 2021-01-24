# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

import pyqrcode
from pyqrcode import QRCode

s = "https://web.stanford.edu/~hastie/Papers/ESLII.pdf"

url = pyqrcode.create(s)

url.svg("book.svg", scale=8)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
