from werobot import WeRoBot
import time
import requests

import config
from utils import tencentai

robot = WeRoBot(token=config.TOKEN)
robot.config["HOST"] = config.HOST
robot.config["PORT"] = config.PORT
robot.config["APP_ID"] = config.APP_ID
robot.config["APP_SECRET"] = config.APP_SECRET

@robot.subscribe
def subscribed(message):
    '''订阅后欢迎语'''
    return config.WelcomeText

@robot.text
def echo(message):
    '''聊天
    调用腾讯AI的接口
    '''
    question = message.content
    #api参数
    params = {
        "app_id": config.APPID,
        "session": "10000",
        "question": question,
        "time_stamp": tencentai.time_stamp(),
        "nonce_str": tencentai.noce_str()
    }
    params["sign"] = tencentai.sign(params_dict=params, appkey=config.APPKEY)
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    response = requests.post(url, data=params)
    result = response.json()
    if result["ret"] != 0:
        text = config.ErrorText + "\n" + result["msg"]
        return text
    return result["data"]["answer"]



robot.run()