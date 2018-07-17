import requests
from bs4 import BeautifulSoup
import time, random

class spider_91():
    def __init__(self):
        self.main_url = 'http://91.91p17.space/video.php?category=rf&page='

    def fake_headers(self):
        randomIP = str(random.randint(0, 255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36Name','Referer':'http://91porn.com','X-Forwarded-For':randomIP}
        return headers
        
    def parse_web(self, page=2):
        url = self.main_url + str(page)
        raw_web =requests.get(url, headers=self.fake_headers(), timeout = 15)
        dic_massage={}
        detail_list=[]
        data = BeautifulSoup(raw_web.text, 'lxml')
        try:
            detail_urls = data.select('div.listchannel')
            for detail in detail_urls:
                title = str(detail.a.img['title'])
                url = str(detail.a['href'])
                img = str(detail.a.img['src'])
                dic_massage[title]=img
                detail_list.append(url)
            print('页面解析完成，准备分析视频地址')
        except:
            print('页面解析出现错误，即将保存页面进行分析')
            f = open('worong_html'+int(time.time())+'.html', 'wb')
            f.write(raw_web.content)
            f.close()
        return (dic_massage,detail_list)

    def get_real_url(self, urls):
        video_urls = []
        num = 1 
        for url in urls:
            web_data = requests.get(url, headers=self.fake_headers())
            soup = BeautifulSoup(web_data.text, 'lxml')
            for i in soup.select('source'):
                if i['src']:
                    video_urls.append(str(i['src']))
                    print('已提取%d个视频'%num)
                    num+=1
                    #time.sleep(random.randint(3,10))
                else:
                    pass
            #print(web_data.request.headers)
        return video_urls
    def run(self, page=2):
        result = self.parse_web(page)
        video_urls = self.get_real_url(result[1])
        print(video_urls)
        print('共有%d个视频被解析'%len(video_urls))
        
        return True
if __name__ == '__main__':
    temp = spider_91()
    flage = ''
    while flage != 'q':
        flage = input('输入要查看的页数,退出输入q\n')
        temp.run(flage)























