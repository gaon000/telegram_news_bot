import dart_fss as dart
import requests
from pymongo import MongoClient
import datetime
my_token = '1360343344:AAHukkz_iEoD1lutw7bj2uA1IzLjrwUOGO8'

cli = MongoClient('localhost', 27017)
db = cli.ncs
collection=db.dart
now = datetime.datetime.now()
today = now.strftime('%Y%m%d')
detail_link = 'http://m.dart.fss.or.kr/html_mdart/MD1007.html?rcpNo='
api = 'https://opendart.fss.or.kr/api/list.json'
'https://opendart.fss.or.kr/api/list.json?crtfc_key={}&corp_code={}&bgn_de={}'
api_key = "27ed4750893e5a91c18217f817a42059f30499e5"
dart.set_api_key(api_key)
url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key={}&corp_code={}"
corp_list=dart.get_corp_list()
def get_number(corpname):
    return corp_list.find_by_corp_name(corpname)[0].to_dict()['corp_code']
print(get_number('삼성전자'))
