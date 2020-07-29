import feedparser
from pymongo import MongoClient
import datetime
from dateutil import parser
import time
import telegram
my_token = '930514973:AAFqVQtB7_igtP85tfAiZY_TVkIjgT0fKn4'
bot = telegram.Bot(token=my_token)


cli = MongoClient('localhost', 27017)
db = cli.ncs
collection_breaknews = db.breaknews
collection_topic = db.topic
collection_topicnews = db.topicnews

a=[]
b=[]
# (t-datetime.datetime(1970,1,1)).total_seconds()
RSS = {
#'머니투데이': 'http://rss.mt.co.kr/mt_news_stock.xml',
#'매일경제':'http://file.mk.co.kr/news/rss/rss_50200011.xml',
#'한국경제':'http://rss.hankyung.com/new/news_stock.xml',
#'이데일리':'http://rss.edaily.co.kr/stock_news.xml',
    'mk': 'https://www.mk.co.kr/rss/40300001/'
    }
# '''

while(1):
	for k, v in RSS.items():
		print(k)
		d = feedparser.parse(v)
		for i in range(len(d['entries'])):
			try:
				a.append(((parser.parse(d['entries'][i]['published']).replace(tzinfo=None) - datetime.datetime(1970,1,1)).total_seconds(), d['entries'][i]['title'], d['entries'][i]['link'], d['entries'][i]['description']))
			except KeyError:
				print("keyerror")
	a.sort(key=lambda element : element[0])
	#	for i in collection_topic.find_one()['topics']:
#		for j in a:
#			if i in j[3]:
#	b.append(j)
                
	for i in a:
		if i[0] > collection_breaknews.find_one()['media']['mk'][0]:
			for j in collection_topic.find_one()['topic']:
				print(j)
				print(i[3])
				if j in i[3]:
					bot.send_message(chat_id=944628369, text=f'topic is {j}\n{i[2]}')
#bot.send_message(chat_id=944628369, text=i)
			if i == a[-1]:
				collection_breaknews.replace_one(collection_breaknews.find_one(), {"media":{"mk":a[-1]}})
	time.sleep(180)
# collection_breaknews.insert_one({"media":{"mk":a[-1]}})
