#urllib基础
import urllib.request
# #urlretrieve(网址,本地文件存储地址) 直接下载网页到本地
#
# # urllib.request.urlretrieve("http://www.baidu.com","D:\\lianxi\\dld.html")
# # urllib.request.urlcleanup()
#看网页相应的简介信息info()
file=urllib.request.urlopen("https://read.douban.com/provider/all")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
result = Request(file, headers=headers)
print(result.info())





from urllib.request import urlopen, Request

url = "https://read.douban.com/provider/all"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
ret = Request(url, headers=headers)
res = urlopen(ret)
aa = res.read().decode('utf-8')
print(aa)




