# 文章下载
import requests
#引用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
# res.encoding='gbk'
#定义Response对象的编码为gbk
text = res.text
#把Response对象的内容以字符串的形式返回
print(text[0:])
#打印小说内容