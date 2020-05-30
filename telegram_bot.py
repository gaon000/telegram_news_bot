from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import feedparser



my_token = '930514973:AAFqVQtB7_igtP85tfAiZY_TVkIjgT0fKn4'

topic = ""

print('start telegram chat bot')
RSS = {
    'DART':'http://dart.fss.or.kr/api/todayRSS.xml',
    '머니투데이': 'http://rss.mt.co.kr/mt_news_stock.xml',
    '매일경제':'http://file.mk.co.kr/news/rss/rss_50200011.xml',
    '한국경제':'http://rss.hankyung.com/new/news_stock.xml',
    '이데일리':'http://rss.edaily.co.kr/stock_news.xml',
    'mk': 'https://www.mk.co.kr/rss/30000001/'
    }

def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)


def help_command(bot, update) :
    update.message.reply_text("명령어 목록?\n1. /subscribe: 구독\n2. /topic {args}: 구독할 topic")

def subscribe_command(bot, update):
    update.message.reply_text("구독되었습니다. /topic명령어를 이용하여 topic을 추가하여주세요.")

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
                bot.send_message(chat_id=update.message.chat_id, text = d['entries'][j]['title'])


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
updater.start_polling(timeout=3, clean=True)
updater.idle()
