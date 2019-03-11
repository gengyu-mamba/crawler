# BeautifulSoup

BeautifulSoup 是一个可以从HTML或XML文件中提取数据的Python库。它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式。

requests库帮我们了解了如何获取数据，而BeautifulSoup能够帮助我们解析和提取数据。

## BeautifulSoup的安装

要安装 BeautifulSoup，Windows用户只要在你的终端中运行这个简单命令即可：
```python
pip install BeautifulSoup4
```
Mac用户只要在你的终端中运行这个简单命令即可：
```python
pip3 install BeautifulSoup4
```

## BeautifulSoup的基本使用

### 解析数据

BeautifulSoup解析数据的用法很简单，示例如下：
```python
bs对象 = BeautifulSoup(要解析的文本,'解析器')
```

在括号中，要输入两个参数，第1个参数是要被解析的文本，注意了，它必须是字符串。括号中的第1个参数用来标识解析器，我们要用的是一个Python内置库：html.parser。（它不是唯一的解析器，但是比较简单的）

我们看看具体的用法。
```python
import requests
from bs4 import BeautifulSoup
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html') 
soup = BeautifulSoup( res.text,'html.parser')
print(type(soup)) #查看soup的类型
print(soup) # 打印soup
```
执行结果：
```python
<class 'bs4.BeautifulSoup'>
# soup内容为解析的htnl网页内容，内容过长，这里不做展示
```

看看运行结果，soup的数据类型是<class 'bs4.BeautifulSoup'>，说明soup是一个BeautifulSoup对象。

下一行开始，就是我们打印的soup，它是我们所请求网页的完整HTML源代码。

可是疑点来了：如果有非常细心的同学，也许会发现，打印soup出来的源代码和我们之前使用response.text打印出来的源代码是完全一样的。

也就是说，我们好不容易用BeautifulSoup写了一些代码来解析数据，但解析出的结果，竟然和没解析之前一样。

你听我解释，事情是这样的：虽然response.text和soup打印出的内容表面上看长得一模一样，但它们属于不同的类：<class 'str'> 与<class 'bs4.BeautifulSoup'>。前者是字符串，后者是已经被解析过的BeautifulSoup对象。之所以打印出来的是一样的文本，是因为BeautifulSoup对象在直接打印它的时候会调用该对象内的str方法，所以直接打印 bs 对象显示字符串是str的返回结果。

我们之后还会用BeautifulSoup库来提取数据，如果这不是一个BeautifulSoup对象，我们是没法调用相关的属性和方法的，所以，我们刚才写的代码是非常有用的，并不是重复劳动。

到这里，你就学会了使用BeautifulSoup去解析数据：
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(字符串,'html.parser') 
```

### 提取数据

我们仍然使用BeautifulSoup来提取数据。

这一步，又可以分为两部分知识：find()与find_all()，以及Tag对象。

先看find()与find_all()。

find()与find_all()是BeautifulSoup对象的两个方法，它们可以匹配html的标签和属性，把BeautifulSoup对象里符合要求的数据都提取出来。

它俩的用法基本是一样的，区别在于，find()只提取首个满足要求的数据，而find_all()提取出的是所有满足要求的数据。

#### find()、find_all()用法
方法     |作用    | 用法  |   示例
-------- | -------- | -------- | -------- 
find()    | 提取满足要求的首个数据 | BeautifulSoup<br>对象find(标签，属性)    | soup.find('div',class_='books')
find_all()| 提取满足要求的所有数据 | BeautifulSoup<br>对象find_all(标签，属性)    | soup.find_all('div',class_='books')

下一步，就是看看Tag类对象的常用属性和方法了。

#### Tag对象的三种常用属性与方法
属性/方法     |作用    
-------- | --------
Tag.find()和Tag.find_all() | 提取Tag中的Tag
Tag.text | 提取Tag中的文字
Tag['属性名'] | 输入参数:属性名,可以提取Tag中这个属性的值
