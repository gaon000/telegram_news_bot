import feedparser

RSS = {
    # 'DART':'http://dart.fss.or.kr/api/todayRSS.xml',
    # '머니투데이': 'http://rss.mt.co.kr/mt_news_stock.xml',
    # '매일경제':'http://file.mk.co.kr/news/rss/rss_50200011.xml',
    # '한국경제':'http://rss.hankyung.com/new/news_stock.xml',
    # '이데일리':'http://rss.edaily.co.kr/stock_news.xml'
    'mk': 'https://www.mk.co.kr/rss/30000001/'
    }
 
for k, v in RSS.items():
    print(k)
    d = feedparser.parse(v)
    for i in range(len(d['entries'])):
        print(d['entries'][i]['title'])
        print(d['entries'][i]['link'])
        
