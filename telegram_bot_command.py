from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import feedparser
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.ncs
collection = db.topic
collection_dart = db.dart

#import dart.dart_api as dart

my_token = '930514973:AAFqVQtB7_igtP85tfAiZY_TVkIjgT0fKn4'
topic = ""

print('start telegram chat bot')
# 중앙, 조선, mk 3분 주기 모니터링
breaknews_rss = {
    '머니투데이': 'http://rss.mt.co.kr/mt_news_stock.xml',
    '매일경제':'http://file.mk.co.kr/news/rss/rss_50200011.xml',
    '한국경제':'http://rss.hankyung.com/new/news_stock.xml',
    '이데일리':'http://rss.edaily.co.kr/stock_news.xml',
    'mk': 'https://www.mk.co.kr/rss/30000001/',
    '중앙일보':'https://rss.joins.com/joins_politics_list.xml',
    '한겨레':'http://www.hani.co.kr/rss/politics/'
    }
topic_rss = {
    
}

def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)


def help_command(bot, update) :
    update.message.reply_text("명령어 목록?\n1. /subscribe: 구독\n2. /topic 키워드: 구독할 topic\n3. /delete 키워드: 삭제할 topic\n4. /dart_topic 키워드: dart 공시 받을 토픽입력\n5. /dart_delete 키워드: dart 토픽 삭제")

def subscribe_command(bot, update):
    update.message.reply_text("구독되었습니다. /topic명령어를 이용하여 topic을 추가하여주세요.")

def fss(bot, update, args):
    pass    

def topic_add_command(bot, update, args):
	topics = "구독한 topic:"
	topic_list = collection.find_one()['topic']
	topic_list = list(set(topic_list+args))
	collection.replace_one(collection.find_one(), {'topic':topic_list})
	for arg in topic_list:
		topics+= '\n - {}'.format(arg)
	bot.send_message(chat_id=944628369, text = topics)

def topic_sub_command(bot, update, args):
	topic_list = collection.find_one()['topic']
	for i in args:
		try:
			topic_list.remove(i)
		except ValueError:
			bot.send_message(chat_id=944628369, text="%s은(는) 구독하지 않은 토픽입니다."%i)
			continue
		bot.send_message(chat_id=944628369, text="%s은(는) 삭제되었습니다."%i)
	collection.replace_one(collection.find_one(), {'topic':topic_list})

def disclosure_topic_add(bot, update, args):
	print(args)
	topics = "구독한 topic:"
	topic_list = collection_dart.find_one()['topic']
	topic_list = list(set(topic_list+args))
	collection_dart.replace_one(collection_dart.find_one(), {'topic':topic_list})
	for arg in topic_list:
		topics+='\n - {}'.format(arg)
	bot.send_message(chat_id=944628369, text = topics)

def disclosure_topic_sub(bot, update, args):
	topic_list = collection_dart.find_one()['topic']
	for i in args:
		try:
			topic_list.remove(i)
		except ValueError:
			bot.send_message(chat_id=944628369, text="%s은(는) 구독하지 않은 토픽입니다."%i)
			continue
		bot.send_message(chat_id=944628369, text = "%s은(는) 삭제되었습니다."%i)
	collection_dart.replace_one(collection_dart.find_one(), {'topic':topic_list})
	

#def print_news(bot, update, args):
 #   for i in topic:
  #      if i in RSS:
   #         d = feedparser.parse(RSS[i])
    #    for j in range(len(d['entries'])):
     #       print(d['entries'][j]['title'])
      #      print(d['entries'][j]['link'])
       #     bot.send_message(chat_id=update.message.chat_id, text = d['entries'][j]['title'])
        #    bot.send_message(chat_id=update.message.chat_id, text = d['entries'][j]['title'])

updater = Updater(my_token)
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('subscribe', subscribe_command))
updater.dispatcher.add_handler(CommandHandler('topic', topic_add_command, pass_args=True)) 
updater.dispatcher.add_handler(CommandHandler('delete', topic_sub_command, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('dart_topic', disclosure_topic_add, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('dart_delete', disclosure_topic_sub, pass_args=True)) 
updater.start_polling(timeout=3, clean=True)
updater.idle()
