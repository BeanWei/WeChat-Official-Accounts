from flask import request, render_template, jsonify, abort, send_from_directory
from app import app

@app.route("/", methods=["GET"])
def index():
    '''首页 公众号二维码'''
    pass

@app.route("/news", methods=["GET"])
def getnews():
    '''爬虫获取实时新闻'''
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
