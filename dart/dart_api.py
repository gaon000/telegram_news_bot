import dart_fss as dart
import requests
api_key = "27ed4750893e5a91c18217f817a42059f30499e5"
dart.set_api_key(api_key)
corp_list=dart.get_corp_list()
url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key={}&corp_code={}"

def get_number(corpname):
    return corp_list.find_by_corp_name(corpname, exactly=True)[0]
print(get_number("삼성전자").to_dict())