from flask import request, render_template, jsonify, abort, send_from_directory

from app import app
from app.spider import news

@app.route("/", methods=["GET"])
def index():
    '''首页 公众号二维码'''
    return "hello"

@app.route("/news", methods=["GET"])
def getnews():
    '''爬虫获取实时新闻'''
    data = news.SinaNews()
    return render_template("list.html", data=data)


@app.route("/news/detail", methods=["GET"])
def nesdetail():
    '''获取新闻详情'''
    # target_url = request.args.get("src")
    # title, cover, content = news.SinaNewsDetail(target_url)
    # return render_template("detail.html", title=title, content=content, cover=cover)
    #页面暂时直接跳转到原页面
    pass


@app.route("/articles",  methods=["GET"])
def getarticles():
    '''获取所有公众号文章'''
    pass

@app.route("/github", methods=["GET"])
def github():
    '''爬虫获取github今日最热开源项目'''
    pass

@app.route("/oschina", methods=["GET"])
def oschina():
    '''爬虫获取oschina今日最热'''
    pass
