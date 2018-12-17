import json
import feedparser
import random

feed = feedparser.parse("http://www.haaretz.com/cmlink/1.4850020")
num = random.randint(0, 10)
title = feed["entries"][num]["title"]
link = feed["entries"][num]["link"]
image = feed["entries"][num]["links"][1]["href"]
print(title)
print(link)
print(image)

var = {
    'title': 'The architecture and human folly of barriers',
    'title_detail': {'type': 'text/plain',
                     'language': None,
                     'base': 'http://www.haaretz.com/cmlink/1.4850020',
                     'value': 'The architecture and human folly of barriers'},
    'links': [{'rel': 'alternate',
               'type': 'text/html',
               'href': 'https://www.haaretz.com/israel-news/MAGAZINE-the-architecture-and-human-folly-of-barriers-1.6740871'},
              {'type': 'image/jpeg',
               'href': 'https://www.haaretz.com/polopoly_fs/1.6740866.1544626059!/image/3699078666.jpg_gen/derivatives/landscape_108/3699078666.jpg',
               'rel': 'enclosure'}],
    'link': 'https://www.haaretz.com/israel-news/MAGAZINE-the-architecture-and-human-folly-of-barriers-1.6740871',
    'summary': 'An exhibition in Tel Aviv focuses on fortifications, from the Great Wall of China, to the Maginot Line, to Israel’s separation barrier',
    'summary_detail': {'type': 'text/html',
                       'language': None,
                       'base': 'http://www.haaretz.com/cmlink/1.4850020',
                       'value': 'An exhibition in Tel Aviv focuses on fortifications, from the Great Wall of China, to the Maginot Line, to Israel’s separation barrier'},
    'id': '1.6740871',
    'guidislink': False, 'published': 'Wed, 12 Dec 2018 17:07:14',
    'published_parsed': None, 'authors': [{'name': 'Moshe Gilad'}],
    'author': 'Moshe Gilad', 'author_detail': {'name': 'Moshe Gilad'},
    'tags': [{'term': 'West Bank', 'scheme': None, 'label': None},
             {'term': 'Israel culture', 'scheme': None, 'label': None},
             {'term': 'Tel Aviv', 'scheme': None, 'label': None}]
}
