from werobot import WeRoBot
import time
import requests

from app import config
from app.utils import tencentai

robot = WeRoBot(token=config.TOKEN)
robot.config["APP_ID"] = config.APP_ID
robot.config["APP_SECRET"] = config.APP_SECRET

client = robot.client

#公众号底栏菜单
client.create_menu({
    "button": [
        {
            "name": "知了",
            "sub_button": [
                {
                    "type": "view",
                    "name": "历史文章",
                    "url": "/news"
                },
                {
                    "type": "view",
                    "name": "今日新闻",
                    "url": "/news"
                }
            ]
        },
        {
            "name": "开源",
            "sub_button": [
                {
                    "type": "view",
                    "name": "Github",
                    "url": "https://github.com/BeanWei"
                },
                {
                    "type": "view",
                    "name": "码云",
                    "url": "https://github.com/BeanWei"
                }
            ]
        },
        {
            "name": "关于",
            "sub_button": [
                {
                    "type": "view",
                    "name": "关于我",
                    "url": "https://github.com/BeanWei"
                },
                {
                    "type": "view",
                    "name": "合作",
                    "url": "https://github.com/BeanWei"
                }
            ]
        }
    ]
})




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
