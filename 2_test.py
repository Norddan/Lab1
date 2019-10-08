import unittest
import codecs
import urllib.request
from bs4 import BeautifulSoup

class Second_test(unittest.TestCase):
    def test_crawler(self):
        urllib.request.urlretrieve("https://stopgame.ru/news", "test.txt")

        with codecs.open("test.txt", "r", encoding="utf-8") as outfile:
            topics = {}
            topics["articles"] = []
            soup3 = BeautifulSoup(outfile, 'html.parser')
            l3 = soup3.find("div", {"class": "lent-left"})
            for i in l3.findAll("div", "title lent-title"):
                topics["articles"].append({"Title": i.text})
        c=0
        list_len = len(topics["articles"])
        while c < list_len:
            art_list = list(topics["articles"][c].values())
            self.assertTrue(art_list)
            c+=1

if __name__ == '__main__':
    unittest.main()