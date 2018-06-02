import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
ua = UserAgent()

def githubproject():
    '''爬取github trending 列表页'''
    headers = {
        'User-Agent'		: ua.random,
        'Accept'			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'	: 'gzip,deflate,sdch',
        'Accept-Language'	: 'zh-CN,zh;q=0.8'
    }
    url = 'https://github.com/trending/python'
    r = requests.get(url, headers=headers)

    d = pq(r.content)
    items = d('ol.repo-list li')

    data = []
    for item in items:
        project = {}
        i = pq(item)
        project["title"] = i("h3 a").text()
        project["owner"] = i("span.prefix").text()
        project["description"] = i("p.col-9").text()
        project["star"] = i("a.muted-link:first").text()
        project["url"] = "https://github.com" + i("h3 a").attr("href")
        data.append(project)
    return data