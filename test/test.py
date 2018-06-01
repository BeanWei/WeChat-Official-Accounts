import time
import hashlib 
import execjs
import requests

def getsignature():
    '''计算今日头条_signature参数'''
    req = requests.Session()
    # js获取目的
    jsurl = 'https://s3a.pstatp.com/toutiao/resource/ntoutiao_web/page/home/whome/home_da59924.js'
    resp = req.get(jsurl)
    ctx = execjs.get().compile((resp.content).decode("utf-8").encode("gbk"))
    js = 'window.TAC.sign(1)'
    signature = ctx.call(js)
    print(signature)
    return signature

getsignature()