from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import feedparser
import dart.dart_api as dart

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
    update.message.reply_text("명령어 목록?\n1. /subscribe: 구독\n2. /topic {args}: 구독할 topic\n3. dart 공시받기")

def subscribe_command(bot, update):
    update.message.reply_text("구독되었습니다. /topic명령어를 이용하여 topic을 추가하여주세요.")

def fss(bot, update, args):
    pass    

def topic_add_command(bot, update, args):
    topics = "구독한 topic:"
    print(args)
    for arg in args:
        topics+= '\n - {}'.format(arg)
    bot.send_message(chat_id=update.message.chat_id, text = topics)
    for i in topic:
        if i in RSS:
            d = feedparser.parse(RSS[i])
            for j in range(len(d['entries'])):
                bot.send_message(chat_id=update.message.chat_id, text = d['entries'][j]['title'])
                bot.send_message(chat_id=update.message.chat_id, text = d['entries'][j]['link'])


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
updater.dispatcher.add_handler(CommandHandler('dart', dart, pass_args=True))
updater.start_polling(timeout=3, clean=True)
updater.idle()
