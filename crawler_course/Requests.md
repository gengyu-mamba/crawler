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
response.text   | 以字符串形式返回响应
response.content  | 以二进制形式返回响应
response.encoding  | 设置响应的编码方式

首先是response.url，示例如下：
```python
import requests 

res_url = requests.get('https://www.csdn.net/')
print(res_url.url)
```
执行结果：
```python
https://www.csdn.net/
```
显而易见，res_url是用来返回请求的网站地址。

接下来的属性是response.status_code，它能够返回请求的响应状态码，示例如下：
```python
import requests 

res_url = requests.get('https://www.csdn.net/')
print(res_url.status_code)
```
执行结果：
```python
200
```

响应状态码200代表服务器同意了我们的请求，并返回了数据给我们。当然，除了200，还有其他响应状态码，下面我列出了常用的一些响应状态码：

#### 常用响应状态吗
响应状态吗     |说明    | 示例  |   说明
-------- | -------- | -------- | -------- 
1xx  | 信息性状态码    | 100    | 继续提出请求
2xx  | 成功状态码      | 200    | 请求成功
3xx  | 重定向状态码    | 305    | 应使用代理访问
4xx  | 客户端错误状态码| 404    | 所请求的页面不存在或已被删除
5xx  | 服务端错误状态码| 503    | 服务不可用

接下来的属性是response.text，它能够以字符串形式返回响应内容，适用于文字、网页源代码的下载。示例如下：
```python
import requests 

res_url = requests.get('https://www.csdn.net/robots.txt')
print(res_url.text)
```
执行结果：
```python
User-agent: *
Disallow: /scripts
Disallow: /public
Disallow: /css/
Disallow: /images/
Disallow: /content/
Disallow: /ui/
Disallow: /js/
Disallow: /scripts/
Disallow: /article_preview.html*
Disallow: /tag/
Disallow: /*?*

Sitemap: http://www.csdn.net/article/sitemap.txt
```
通过response.text方法，我们可以获取我们想要的内容，将其打印或者存储起来。

接下来的属性是response.content，它能够以二进制形式返回响应内容，适用于图片、音频、视频的下载。如果我们想下载一张图片，它的URL是：https://goss3.vcg.com/creative/vcg/800/version23/VCG41549445817.jpg
![person](https://goss3.vcg.com/creative/vcg/800/version23/VCG41549445817.jpg)

示例如下：
```python
import requests

res_url = requests.get('https://goss3.vcg.com/creative/vcg/800/version23/VCG41549445817.jpg')
img = res_url.content
image = open('person.jpg','wb')
image.write(img)
image.close()
```

这样，我们需要的图片就下载到本地了。

最后一个属性是response.encoding，它能够设置响应的编码方式。示例如下:
```python
import requests 

res_url = requests.get('https://edu.csdn.net/notebook/python/week01/1.html')
res_url.encoding = 'gbk'
print(res_url.text)
```

执行后，发现网站内容出现一堆乱码，这是怎么回事呢？

原来，这个网站的数据类型是UTF-8，当我们设置编码格式为GBK后，造成其与本身的UTF-8编码不一致，所以打印出来一堆乱码。

在现实情况中，我们应当在何时使用response.encoding呢？
首先，目标数据本身是什么编码是未知的。用requests.get()发送请求后，我们会取得一个Response对象，其中，requests库会对数据的编码类型做出自己的判断。但是！这个判断有可能准确，也可能不准确。

如果它判断准确的话，我们打印出来的response.text的内容就是正常的、没有乱码的，那就用不到res.encoding；如果判断不准确，就会出现一堆乱码，那我们就可以去查看目标数据的编码，然后再用res.encoding把编码定义成和目标数据一致的类型即可。

好了，到这里，Requests.get()和Response的属性就讲完了。
























