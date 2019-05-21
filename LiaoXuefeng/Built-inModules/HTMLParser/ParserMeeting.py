from html.parser import HTMLParser
from urllib import request
import re
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.CurrentDate = ""

    def handle_starttag(self, tag, attrs):
        if ("class", "event-title") in attrs:
            self.CurrentDate = "title"
        elif tag == "time":
            self.CurrentDate = "time"
        elif ("class", "say-no-more") in attrs:
            self.CurrentDate = "year"
        elif ("class", "event-location") in attrs:
            self.CurrentDate = "address"

    def handle_endtag(self, tag):
        self.CurrentDate = ""

    def handle_data(self, data):
        if self.CurrentDate == "title":
            print("****Meeting****")
            print("title: %s" % data)
        elif self.CurrentDate == "time":
            print("time: %s" % data)
        elif self.CurrentDate == "year":
            if re.match(r'\s\d{4}', data): # 因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                print("year: %s" % data.strip())
        elif self.CurrentDate == "address":
            print("address: %s" % data)
            
parser = MyHTMLParser()
URL = 'https://www.python.org/events/python-events/'
with request.urlopen(URL, timeout=15) as f:
    data = f.read()
parser.feed(data.decode('utf-8'))