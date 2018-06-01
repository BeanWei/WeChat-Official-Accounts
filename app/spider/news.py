import time
import hashlib 
import execjs
import requests

import common

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

getsignature()