import requests
import json
from datetime import datetime
import database

class api_request_nbu():

    def request_nbu_cours_today(self):
        current_datetime = datetime.strftime(datetime.now(),('%Y%m%d'))
        #  https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?&date=20210108
        nbu_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?&date={0}&json".format(current_datetime)
        r = requests.get(nbu_url)
        j = json.loads(r.text)

        return j

    def request_nbu_cours_day(self):
        pass

    def request_nbu_cours_month(self):
        pass

# nbu_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20200302&json"
# r = requests.get(nbu_url)
# j = json.loads(r.text)
# print(j)

# o = api_request_nbu()
#
#
# name_table = ("nbu")
# columns_table= ("r, txt, rate, cc, exchangedate")
#
#
# c1 = database
#
# for x in o.request_nbu_cours_today():
#     val = (x['r030'], x['txt'], x['rate'], x['cc'], x['exchangedate'])
#     sql = "INSERT INTO nbu ( r, txt, rate, cc, exchangedate) VALUES (%s,%s,%s,%s,%s)"
#     c1.db().insert(name_table,columns_table,val)
#     print(val)






