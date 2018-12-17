from bottle import route, run, template, static_file
import json
import feedparser
import random

@route('/', method='GET')
def index():
    return template("index.html", root='')

@route('/css/<filename:re:.*\.css>' , method='GET')
def stylesheets(filename):
    return static_file(filename, root='static/css')


@route('/getArticles', method='GET')
def index():
    feed = feedparser.parse("http://www.haaretz.com/cmlink/1.4850020")
    num = random.randint(0, len(feed["entries"]))
    articles = []
    for num in range(num, num + 6):
        title = feed["entries"][num]["title"]
        link = feed["entries"][num]["link"]
        image = feed["entries"][num]["links"][1]["href"]
        articles.append({'title': title, 'link': link, 'image': image})
    return json.dumps(articles)

def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
