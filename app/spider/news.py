import time
import hashlib 
import execjs
import requests
import re
from fake_useragent import UserAgent
ua = UserAgent()

from app.spider import common

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
            article["mthumbs"] = i["mthumbs"][0]    #新闻封面
            data.append(article)
        except:
            continue
    return data


def SinaNewsDetail(sina_surl):
    '''获取新浪新闻详情'''
    response = requests.get(sina_surl)
    title = re.findall(r'<h1 class="art_tit_h1">(.*?)</h1>', response.text)[0]
    cover = re.findall(r'<img class="sharePic hide" src="(.*?)"/>', response.text)[0]
    content = re.findall(r'<img class="sharePic hide" src=.*?/>(.*?)<script type="text/javascript">', response.text, re.S|re.M|re.I)[0]
    return title, cover, content



#TODO:分析今日头条的_signature参数

def getNews():
    json_url = "https://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=%s&cp=%s&_signature=%s"
    _as, _cp = get_as_cp()
    signature = getsignature()
    print(_as, _cp, signature)
    url = json_url % (_as, _cp, signature)
    jsonvalues = common.getJsonValues(url=url)
    data = []; article = {}
    for i in jsonvalues["data"]:
        if "chinese_tag" in i.keys():
            continue
        article["title"] = i["title"]
        pass




def get_as_cp():
    '''获取今日头条as和cp的参数'''
    zz ={}
    now = round(time.time())
    e = hex(int(now)).upper()[2:]  #hex()转换一个整数对象为十六进制的字符串表示
    i = hashlib.md5(str(int(now))).hexdigest().upper() #hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    if len(e)!=8:
        zz = {'as': "479BB4B7254C150",
            'cp': "7E0AC8874BB0985"}
        return zz
    n=i[:5]
    a=i[-5:]
    r = ""
    s = ""
    for i in range(5):
        s = s+n[i]+e[i]
    for j in range(5):
        r = r+e[j+3]+a[j]
    zz = {
            'as': "A1" + s + e[-3:],
            'cp': e[0:3] + r + "E1"
        } 
    return zz['as'], zz['cp']

def getsignature():
    '''计算今日头条_signature参数'''
    req = requests.Session()
    # js获取目的
    jsurl = 'https://s3a.pstatp.com/toutiao/resource/ntoutiao_web/page/home/whome/home_da59924.js'
    resp = req.get(jsurl)
    ctx = execjs.get().compile(resp.content)
    js = 'window.TAC.sign(1)'
    signature = ctx.eval(js)
    print(signature)
    return signature



