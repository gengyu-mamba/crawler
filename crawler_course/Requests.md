# Requests

获取网页内容的相关模块有很多，例如：Requests，urllib3等等。这里我们使用Requests模块。

Requests是一个方便易用的HTTP请求库，它比python自带的urllib要更方便更快捷，十分适合爬虫初学者。

## Requests的安装

要安装 Requests，Windows用户只要在你的终端中运行这个简单命令即可：
```python
pip install requests
```
Mac用户只要在你的终端中运行这个简单命令即可：
```python
pip3 install requests
```

## Requests的基本使用

发送Get请求

```python
# 导入requests模块
import requests
# requests.get()方法向服务器发送请求，括号里的参数是你需要的数据所在的网址，服务器作出响应后将响应数据赋值给res_url。
res_url = requests.get('url')
```

那么我们获取的res_url是个什么对象呢？
```python
import requests 

res_url = requests.get('https://www.csdn.net/')
print(type(res_url)) # type():返回对象的类型
```
执行结果：
```python
<class 'requests.models.Response'>
```

res_url属于requests.models.Response类。所以，res_url是一个Response对象。我们也就可以去了解它的属性和方法了。

Response对象的常用属性如下：

属性     | 作用
-------- | -----
response.url  | 返回请求网站的URL
response.status_code  | 返回响应状态码
response.encoding  | 返回响应的编码方式
response.content  | 以二进制形式返回响应
response.text   | 以字符串形式返回响应

首先是response.url，代码如下：















