# -*- coding: utf-8 -*-
# User: 
# Date: 2020/6/27
"""
作业一：
安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# 电影网址
url = 'https://maoyan.com/films?showType=3'
request_settings = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Accept': "*/*",
    'Accept-Encoding': 'gazip, deflate, br',
    'Accept-Language': 'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
    'Content-Type': 'text/plain',
    'Connection': 'keep-alive',
    # 'Host': 'wreport1.meituan.net',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/films?showType=3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}
header = {}
header['user-agent'] ='ccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
                      'Accept-Encoding: gzip, deflate, br' \
                      'Accept-Language: zh-CN,zh;q=0.9' \
                      'Cache-Control: max-age=0' \
                      'Connection: keep-alive' \
                      'Cookie: __mta=213325355.1593353964202.1593357558460.1593357570208.25; uuid_n_v=v1; uuid=5CCA1F10B94A11EA95E3C92BBC8FF019CE66C0659AF94DF6890C2A2A177CD4CF;' \
                      ' _csrf=8b53d39d5a34d3c2729725c3812094fa021c70ca8c1500652c255555257ca719; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593353964; _lxsdk_cuid=172fb4c08bb23-0d94b' \
                      '1fd03768e-4353760-1fa400-172fb4c08bcc8; _lxsdk=5CCA1F10B94A11EA95E3C92BBC8FF019CE66C0659AF94DF6890C2A2A177CD4CF; mojo-uuid=8e22943cba5928ebdcac3544636feae6; ' \
                      'mojo-session-id={"id":"ba562948c63dad2d431421d90ae72830","time":1593355942857}; mojo-trace-id=27; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593357786; ' \
                      '__mta=213325355.1593353964202.1593357570208.1593357786222.26; _lxsdk_s=172fb6a2d1c-c3c-67a-966%7C%7C52' \
                      'Host: maoyan.com' \
                      'Sec-Fetch-Dest: document' \
                      'Sec-Fetch-Mode: navigate' \
                      'Sec-Fetch-Site: none' \
                      'Sec-Fetch-User: ?1' \
                      'Upgrade-Insecure-Requests: 1' \
                      'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'


# header['user-agent'] =    'Accept: */*' \
#                            'Accept-Encoding: gzip, deflate, br' \
#                            'Accept-Language: zh-Hans-CN, zh-Hans; q=0.5' \
#                            'Cache-Control: no-cache' \
#                            'Host: s3plus.meituan.net' \
#                            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
# header['user-agent'] = request_settings
response = requests.get(url, headers=header)
bs_info = bs(response.text, 'html.parser')

counter = 0
movieList = []
movieName = None
movieType = None
movieShowTime = None
print(bs_info)
for movie_info in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    print(movie_info)
    if counter > 10:
        counter += 1
        break
    # 获取电影名字
    movieName = movie_info.find('span', attrs={'class': 'name'}).text
    span = movie_info.find('span')
    # 获取电影类型，未调试完
    movieType = movie_info.find('span', attrs={'class': 'hover-tag'}).text
    # 获取电影上映时间,未调试完
    movieShowTime = movie_info.find('span').text

    movieList.append({'movieName': movieName, 'movieType': movieType, 'movieShowTime': movieShowTime})


movie1 = pd.DataFrame(data=movieList)
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)