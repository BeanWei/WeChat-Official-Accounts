import time
import hashlib 
import execjs
import requests
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 

from fake_useragent import UserAgent
ua = UserAgent()


def SinaNews():
    '''获取新浪科技新闻列表'''
    json_url = "http://cre.mix.sina.com.cn/api/v3/get?callback=jQuery111203503056714736408_1527899632664&cateid=1z&cre=tianyi&mod=pctech"
    headers = {
        "User-Agent": ua.random
    }
    response = requests.get(json_url, headers=headers).text
    jsonvalues = eval(re.findall(r'{"data":(.*?),"status"', response)[0])
    data = []
    for i in jsonvalues:
        article = {}
        try:
            article["title"] = i["title"]           #新闻标题
            article["intro"] = i["intro"]           #新闻摘要
            article["surl"] = i["surl"]             #新闻链接
            data.append(article)
        except:
            continue
    return data

SinaNews()