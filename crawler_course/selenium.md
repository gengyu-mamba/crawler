# Selenium

selenium是什么呢？它是一个强大的Python库。

它可以做什么呢？它可以用几行代码，控制浏览器，做出自动打开、输入、点击等操作，就像是有一个真正的用户在操作一样。

selenium能控制浏览器，这对解决我们刚刚提出的那几个问题，有什么帮助呢？

首先，当你遇到验证码很复杂的网站时，selenium允许让人去手动输入验证码，然后把剩下的操作交给机器。

而对于那些交互复杂、加密复杂的网站，selenium问题简化，爬动态网页如爬静态网页一样简单。

不论数据存在哪里，浏览器总是在向服务器发起各式各样的请求，当这些请求完成后，它们会一起组成开发者工具的Elements中所展示的，渲染完成的网页源代码。

在遇到页面交互复杂或是URL加密逻辑复杂的情况时，selenium就派上了用场，它可以真实地打开一个浏览器，等待所有数据都加载到Elements中之后，再把这个网页当做静态网页爬取就好了。

说了这么多优点，使用selenium时，当然也有美中不足之处。

由于要真实地运行本地浏览器，打开浏览器以及等待网渲染完成需要一些时间，selenium的工作不可避免地牺牲了速度和更多资源，不过，至少不会比人慢。

知道了它的优缺点，我们就开始学习如何使用selenium吧。

## Selenium的安装

要安装 Selenium，Windows用户只要在你的终端中运行这个简单命令即可：
```python
pip install selenium
```
Mac用户只要在你的终端中运行这个简单命令即可：
```python
pip3 install selenium
```

selenium的脚本可以控制所有常见浏览器的操作，在使用之前，需要安装浏览器的驱动。

我推荐的是Chrome浏览器，打开下面的链接，就可以下载Chrome的安装包了，Windows和Mac都有。

https://localprod.pandateacher.com/python-manuscript/crawler-html/chromedriver/ChromeDriver.html

在正式开始知识的讲解之前，我想首先让你体验一下selenium脚本程序在你的本地终端运行的效果。因为在学习selenium之初，如果能亲自看到浏览器自动弹出后的操作效果，对你后续的学习会有很大帮助。

下面的代码，你现在不需要去理解具体的意思，等会儿就会学到每一行的用法。

现在只需要把这段代码复制到本地的代码编辑器中运行，体验一下你的浏览器为你自动工作的效果。当然，前提是你已经安装好了selenium库以及Chrome浏览器驱动。

```python
# 本地Chrome浏览器设置方法
from selenium import  webdriver 
import time

driver = webdriver.Chrome() 
driver.get('https://www.baidu.com/') 
time.sleep(2)

question = driver.find_element_by_id('kw')
question.send_keys('selenium')
time.sleep(1)
button = driver.find_element_by_id('su')
time.sleep(1)
button.click()
time.sleep(5)
driver.close()
```

除了看程序运行，不如手动打开这个网站看看，做一遍和程序中一样的操作。

## 设置浏览器引擎
和以前一样，使用一个新的Python库，首先要调用它。selenium有点不同，除了调用，还需要设置浏览器引擎。
```python
# 本地Chrome浏览器设置方法
from selenium import webdriver #从selenium库中调用webdriver模块
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
```

以上就是浏览器的设置方式：把Chrome浏览器设置为引擎，然后赋值给变量driver。driver是实例化的浏览器，在后面你会总是能看到它的影子，这也可以理解，因为我们要控制这个实例化的浏览器为我们做一些事情。

配置好了浏览器，就可以开始让它帮我们干活啦！

接下来，我们学习selenium的具体用法。

我们还是按照爬虫的四个步骤来讲解selenium的用法，看看selenium如何获取、解析与提取数据。由于本章节中提取出的数据都不太复杂，直接在终端打印就好，不会涉及到储存数据这一步。

## 获取数据
首先看一下获取数据的代码怎么写吧。

```python
# 本地Chrome浏览器设置方法
from selenium import  webdriver 
import time

driver = webdriver.Chrome() 
driver.get('https://www.baidu.com/') 
time.sleep(2)
```

前面两行代码都是你学过的，调用模块，并且设置浏览器，只有后两行代码是新的。

get(URL)是webdriver的一个方法，它的使命是为你打开指定URL的网页。

刚才说过driver在这里是一个实例化的浏览器，因此，就是通过这个浏览器打开网页。

当一个网页被打开，网页中的数据就加载到了浏览器中，也就是说，数据被我们获取到了。

driver.close()是关闭浏览器驱动，每次调用了webdriver之后，都要在用完它之后加上一行driver.close()用来关闭它。

就像是，每次打开冰箱门，把东西放进去之后，都要记得关上门，使用selenium调用了浏览器之后也要记得关闭浏览器。

