import requests
from bs4 import BeautifulSoup
import time


def parse_web(url):
    raw_web =requests.get(url, headers=headers)
    dic_massage={}
    detail_list=[]
    data = BeautifulSoup(raw_web.text, 'lxml')
    detail_urls = data.select('div.listchannel')
    for detail in detail_urls:
        title = str(detail.a.img['title'])
        url = str(detail.a['href'])
        img = str(detail.a.img['src'])
        dic_massage[title]=img
        detail_list.append(url)
    print('页面解析完成，准备分析视频地址')
    return (dic_massage,detail_list)

def get_real_url(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    #print(soup)
    temp_url = []
    for i in soup.select('textarea.fullboxtext'):
        if i != '': 
            temp_url.append(i.get_text())
    if len(temp_url) == 0:
        print('未分析出html5代码，将保存当前页面进行分析')
        f=open('D:\python_file\my91\wrong.html', 'wb')
        f.write(web_data.content)
        f.close()
        return False
    print('视频地址分析完成，共有%d个视频'%len(temp_url))
    for url in temp_url:
        print('web_site', url)
        if len(url) > 10:
            print('正在分析')
            web_data = requests.get(url, headers = headers)
            soup = BeautifulSoup(web_data.text, 'lxml')
            for i in soup.select('source'):
                if i['src']:
                    print(i['src'])
        else:
            print('wrong', url)
if __name__ == '__main__':
    page = 2
    main_url = 'http://92.91p08.space/video.php?category=rf&page='+str(page)
    headers = {"Accept-Language": "zh-CN",'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    temp = parse_web(main_url)
    url_list = temp[1]
    for url in url_list:
        print(url)
        get_real_url(url)
        
























