#-*- coding = utf-8 -*-
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

#response = urllib.request.urlopen(url="http://www.baidu.com")
#print(response.read().decode("utf-8"))

#response = urllib.request.urlopen(url="http://www.httpbin.org/post",data=data)

#print(response.read().decode("utf-8"))
#print(response.getheaders())
#response = urllib.request.Request(url,headers)
num = 1
url = "https://guba.eastmoney.com/news,tzbd,956902355.html"
#"https://guba.eastmoney.com/list,601216_%s.html" % num
#"https://guba.eastmoney.com/list,601216.html"
#"http://hq.sinajs.cn/list=sh601006"
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")


#response = urllib.request.urlopen(res)
#print(response.read().decode("utf-8"))

#def name_is_exists(tag):
#    return tag.has_attr("div")

def askURL(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"
        }
    res = urllib.request.Request(url=url,headers=headers)
    reponse = urllib.request.urlopen(res)
    html = reponse.read().decode("utf-8")
    return html

def getData():
    dataList = []
    for i in range(10):
        #url = 
        html = askURL(url)



html = askURL(url)
bs = BeautifulSoup(html,"html.parser")
#print(bs.title.contents[0])
op = open("eastmoney1.txt","w")
op.write(str(bs))
#print(bs.find_all(text=re.compile("新闻")))
# print(bs.select('title'))#标签
# print(bs.select('#id'))#idchazhao
# print(bs.select('.da'))#类名查找
# print(bs.select("a[class='']"))
# print(bs.select('head>tital'))
#print(bs.find_all(re.compile("div")))
#t_list = bs.find_all("title")
#print(t_list)
