from Lab1.Finder import get_html_page, find_articles, publish_report

url3="https://stopgame.ru/news"
resp3 = get_html_page(url3)
top = find_articles(resp3, url3)
publish_report(top)
#render_template('news.html', articles=articles)