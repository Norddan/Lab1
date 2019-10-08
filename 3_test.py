import  unittest
import requests

class Third_test(unittest.TestCase):
    def test_url(self):
        url = "https://stopgame.ru/news"
        resp = requests.get(url)
        self.assertEqual(resp.status_code,200)

if __name__ == '__main__':
    unittest.main()