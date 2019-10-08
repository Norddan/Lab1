import requests
from bs4 import BeautifulSoup
import json
import codecs
import datetime
from flask import Flask, render_template

#app = Flask(__name__)
#@app.route('/')

def get_html_page(url):
    resp = requests.get(url)
    return resp
def find_articles(resp, url):
    topics = {}
    now = datetime.datetime.now()
    topics["url"] = [url]
    topics["creationDate"] = [str(now)]
    topics["articles"] = []
    resp = requests.get(url)
    if resp.status_code == 200:
        soup3 = BeautifulSoup(resp.text, 'html.parser')
        l3 = soup3.find("div", {"class": "lent-left"})
        for i in l3.findAll("div", "title lent-title"):
            topics["articles"].append({"Title": i.text})
    else:
        print("All for now")
    return topics
def publish_report(topics):
    with codecs.open("StopGame.json", "w", encoding="utf-8") as outfile:
        json.dump(topics, outfile, indent=4, ensure_ascii=False, separators=(',', ': '))
    outfile.close()


'''def main():
    url3="https://stopgame.ru/news"
    resp3 = get_html_page(url3)
    top = find_articles(resp3)
    publish_report(top)
    #render_template('news.html', articles=articles)'''


'''if __name__=="__main__":
    #app.run(host='localhost', port=8000)
    main()'''