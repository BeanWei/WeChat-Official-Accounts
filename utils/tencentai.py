'''
腾讯AI接口参数获取
'''

import time
import string
import random
import hashlib
from urllib import parse


def time_stamp(): 
    '''获取当前10位时间戳'''
    return int(time.time())

def noce_str():
    '''获取16位随机字符'''
    rule = string.ascii_lowercase + string.digits
    str = random.sample(rule, 32)
    return "".join(str)

def sign(params_dict, appkey):
    '''获取签名'''
    strs = ""
    for k in sorted(params_dict.keys()):
        if strs:
            strs += "&" + k + "=" + parse.quote_plus(str(params_dict[k]).encode("utf-8"))
        else:
            strs += k + "=" + parse.quote_plus(str(params_dict[k]).encode("utf-8"))
    sign_str = str_md5(strs + "&app_key=" + appkey)
    return sign_str

def str_md5(rawstr):
    '''md5加密'''
    hash = hashlib.md5()
    hash.update(bytes(rawstr, encoding="utf-8"))
    return hash.hexdigest().upper()
