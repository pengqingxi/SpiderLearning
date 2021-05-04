#获取http请求信息
import urllib.request as rst
rsp = rst.urlopen('https://www.python.org/')
print(rsp.status)
print(rsp.getheaders())
print(rsp.getheader('Server'))

#通过验证爬取网页
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'pengqingxi'
password = 'pqx123'
url = 'http://pythonscraping.com/pages/auth/login.php'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

#使用代理爬取网页
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:54275',
    'https':'https://127.0.0.1:54275'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.python.org/')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
	
#处理异常
from urllib import request, error
try:
    response = request.urlopen('http://1000.com/index1.shtml')
except error.URLError as e:
    print(e.reason)
	
#使用requests模块发起get请求
import requests
r = requests.get('http://httpbin.org/get')
print(r.text)

#使用requests模块发起带参数的get请求
import requests
data = {
    'name':'pengqingxi',
	'password':'pqx123'
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)

#使用requests抓取图片并保存本地
import requests

r = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
with open('PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png', 'wb') as f:
    f.write(r.content)


#post方法带参数发起请求
import requests

data = {'name':'penqingxi','password':'pqx123'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)

#post方法实现文件上传
import requests

files = {'file':open('baidu.png', 'rb')}
r = requests.post('http://httpbin.org/post',files=files)
print(r.text)


#用match()进行匹配
import re

content = 'Wuhan 10 million_Demographic'
print(len(content))
result = re.match('^Wuhan\s\d\d\s\w{10}',content)
print(result)
print(result.group())
print(result.span())

#BeautifulSoup将错误的html改正
from bs4 import BeautifulSoup
broken_html ＝ ’<ul class=country><li>Area<li>Population</ul>'
# parse the HTML
soup = BeautifulSoup(broken_html,'html.parser')
fixed_html = soup.prettify()
print fixed_html

	
#获取某校学校要闻目录页
import requests

url = 'http://www.wdu.edu.cn/xwzx/xxyw/'
response = requests.get(url)
response.encoding = 'gb2312'
if response.status_code == 200:
    print(response.text)

#获取目录页中的链接
import requests

url = 'http://www.wdu.edu.cn/xwzx/xxyw/'
response = requests.get(url)
response.encoding = 'gb2312'
if response.status_code == 200:
    catalog_html = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(catalog_html,'lxml')
link = []
for div in soup.find_all(name='div',attrs={"class":"wbz_title"}):
    strhref = div.find(name='a').get('href')    
    link.append('http://www.wdu.edu.cn/xwzx/xxyw' + strhref.lstrip('.')) 
print(link)

#获取新闻详情页
import requests

url = 'http://www.wdu.edu.cn/xwzx/xxyw/'
response = requests.get(url)
response.encoding = 'gb2312'
if response.status_code == 200:
    catalog_html = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(catalog_html,'lxml')
link = []
for div in soup.find_all(name='div',attrs={"class":"wbz_title"}):
    strhref = div.find(name='a').get('href')    
    link.append(url + strhref.lstrip('./')) 

for href in link:
    responseDetail = requests.get(href)
    responseDetail.encoding = 'gb2312'
    if responseDetail.status_code == 200:
        detail_html = responseDetail.text
        soupDetail = BeautifulSoup(detail_html,'lxml')
        div = soupDetail.find(name='div',attrs={'class':'TRS_Editor'})
        news = div.find(name='p').text  
        print(news)
