import requests
from bs4 import BeautifulSoup
import sys,os,csv,io
import requests
import json
import pandas as pd
import chardet

class market():

    column = ['symbol', 'code', 'name', 'current', 'percent', 'change', 'high', 'low', 'high52w', 'low52w', 'marketcapital',
          'amount', 'type', 'pettm', 'volume', 'hasexist']
    stu = pd.DataFrame(columns=column)

    def __init__(self):  # 类的初始化操作

        # self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        #
        #                           '(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}  # 给定义一个请求头来模拟EDGE



        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "Connection": "keep-alive",
            "Cookie": "aliyungf_tc=AQAAANinWTSHCw8AfnmCdzSFxRVmxmiI; acw_tc=2760827315673429540042287ef1b0f829da7fec2949f940080f8499185fd1; s=dd12m5iwgu; Hm_lvt_1db88642e346389874251b5a1eded6e3=1567343201; device_id=aa2bd32339fe4bd5a8485cddd98be51b; xq_token_expire=Thu%20Sep%2026%202019%2021%3A08%3A46%20GMT%2B0800%20(China%20Standard%20Time); bid=c842756e38637e05d92b2bd8e8f0b184_k00zrjbq; __utma=1.1267291292.1567343353.1567343353.1567343353.1; __utmc=1; __utmz=1.1567343353.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lpvt_1db88642e346389874251b5a1eded6e3=1567343724; xq_a_token=75661393f1556aa7f900df4dc91059df49b83145; xq_r_token=29fe5e93ec0b24974bdd382ffb61d026d8350d7d; u=641567354778054",
            "Host": "xueqiu.com",
            "Referer": "https://xueqiu.com/hq",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

        # self.web_url = 'https://www.bilibili.com/'

        module_path = os.path.dirname(__file__)

        path = module_path + '/config.xml'

        configfile = io.open(path, encoding='utf-8')

        pathinfo = BeautifulSoup(configfile, 'xml')

        self.photo_path = pathinfo.find('picpath').text.strip()

        # self.crawlerlogging = crawlerlog()

    def retrieve_stock_list(self):
        for i in range(1, 185):
             url = 'https://xueqiu.com/stock/cata/stocklist.json?page=' + str(i) + \
                   '&size=30&order=desc&orderby=percent&type=0%2C1%2C2%2C3&isdelay=1&_=1541211687220'

             response = requests.get(url=url, headers=self.headers)

             data = json.loads(response.text)
        # print(data)

        for b in data['stocks']:

            num = 0

            dict_ = []
            for a in self.column:
              dict_.append(b[a])
              num = num + 1
              dicts = []
              dicts.append(dict_)
              ans = pd.DataFrame(dicts, columns=self.column)
              stu = stu.append(ans)
         # print stu
        print
        stu
        stu.index = range(len(stu))
        stu.to_csv("All.csv", encoding="utf_8_sig")




