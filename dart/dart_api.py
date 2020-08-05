import dart_fss as dart
import requests
from pymongo import MongoClient
import datetime
import telegram
import time
recent = {}
my_token = '930514973:AAFqVQtB7_igtP85tfAiZY_TVkIjgT0fKn4'
bot = telegram.Bot(token=my_token)

cli = MongoClient('localhost', 27017)
db = cli.ncs
collection=db.dart
now = datetime.datetime.now()
today = now.strftime('%Y%m%d')
detail_link = 'http://m.dart.fss.or.kr/html_mdart/MD1007.html?rcpNo='
api_key = "27ed4750893e5a91c18217f817a42059f30499e5"
dart.set_api_key(api_key)
url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key={}&corp_code={}"
corp_list=dart.get_corp_list()

#get corp code
def get_number(corpname):
    return corp_list.find_by_corp_name(corpname)[0].to_dict()['corp_code']

while 1:
	for i in collection.find_one()['topic']:
	#	try:
		print(i)
		print(today)
		corp_code = get_number(i)
		api = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={api_key}&corp_code={corp_code}&bgn_de={today}"
		print(api)
		res = requests.get(api).json()
		status = res['status']
		if status == '013':
			print('continue')
			continue
		elif status == '000':
			if i not in recent:
				for j in reversed(res['list']):
					bot.send_message(chat_id=944628369 ,text=f"종목: {i}\n공시명: {j['report_nm']}\n공시보기: {detail_link+j['rcept_no']}")
				recent[i] = res['list'][0]['rcept_no']
			else:
				if recent[i] == res['list'][0]['rcept_no']:
					continue
				for j in reversed(res['list']):
					if recent[i] < j['rcept_no']:
						bot.send_message(chat_id=944628369, text=f"종목: {i}\n공시명: {j['report_nm']}\n공시보기: {detail_link+j['rcept_no']}")
				recent[i] = res['list'][0]['rcept_no']
		else:
			bot.send_message(chat_id=944628369, text=f"status: {status}")
	time.sleep(600)
	
"""
		except:
			bot.send_message(chat_id=944628369, text=f'종목 {i}를 확인해주세요.')
"""
			
