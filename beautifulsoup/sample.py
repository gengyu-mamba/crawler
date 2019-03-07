# 豆瓣电影爬虫

# 问题需求就是把豆瓣TOP250里面的 序号/电影名/评分/推荐语/链接 都爬取下来，结果就是全部展示打印出来

# 接下来我们一起分析网页吧～
# 进入首页 https://movie.douban.com/top250?start=0&filter= ，打开检查工具，在Elements里查看这个网页，是什么结构。点击开发者工具左上角的小箭头，选中“肖申克的救赎”，这样就定位了电影名的所在位置，审查元素中显示<span class="title">：<span>标签内的文本，class属性；推荐语和评分也是如此，<span class='ing'>，<span class='rating_num'>；序号：<em class>，<em>标签内的文本，class属性；推荐语<span class='ing'>；链接是<a>标签里href的值。最后，它们最小共同父级标签，是<li>。
# 我们再换个电影验证下找的规律是否正确。
# check后，我们再看一共10页，每页的url有什么相关呢？
# 第1页：https://movie.douban.com/top250?start=0&filter=
# 第3页：https://movie.douban.com/top250?start=50&filter=
# 第7页：https://movie.douban.com/top250?start=150&filter=
# 发现只有start后面是有变化哒，规律就是第N页，start=(N-1)*25

# 思路一：先爬取最小共同父级标签 <li>，然后针对每一个父级标签，提取里面的序号/电影名/评分/推荐语/链接。

import requests
from bs4 import BeautifulSoup

for i in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(25*i) + '&filter='
    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')
    movie_items = soup.find_all('div', class_ = 'item')
    for item in movie_items:
        serial_number = item.find('div', class_ = 'pic').find('em').text.strip()
        movie_name = item.find('div', class_ = 'info').find('div', class_ = 'hd').find('a').text.replace('\n', '').replace('\xa0', '')
        movie_score = item.find('div', class_ = 'info').find('div', class_ = 'bd').find('div', class_ = 'star').find('span', class_ = 'rating_num').text.strip()
        if item.find('div', class_ = 'info').find('div', class_ = 'bd').find('p', class_ = 'quote') != None:
            movie_comment = item.find('div', class_ = 'info').find('div', class_ = 'bd').find('p', class_ = 'quote').text.strip()
        else:
            movie_comment = '该电影没有评论'
        movie_url = item.find('div', class_ = 'info').find('div', class_ = 'hd').find('a')['href'].strip()
        print('serial_number:' + serial_number + '\n' + 'movie_name:' + movie_name + '\n' + 'movie_score:' + movie_score + '\n' + 'movie_comment:' + movie_comment + '\n' + 'movie_url:' + movie_url + '\n\n')