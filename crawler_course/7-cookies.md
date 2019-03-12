# Cookies

## post请求

其实，post和get都可以带着参数请求，不过get请求的参数会在url上显示出来。

但post请求的参数就不会直接显示，而是隐藏起来。像账号密码这种私密的信息，就应该用post的请求。如果用get请求的话，账号密码全部会显示在网址上，这显然不科学！你可以这么理解，get是明文显示，post是非明文显示。

通常，get请求会应用于获取网页数据，比如我们之前学的requests.get()。post请求则应用于向网页提交数据，比如提交表单类型数据（像账号密码就是网页表单的数据）。

get和post是两种最常用的请求方式，除此之外，还有其他类型的请求方式，如head、options等，这里我们就不详讲了，因为一般很少用到。

现在，get和post这两种请求方式的区别弄懂了吧？我们继续往下看——

关于【headers】面板里的几个参数，在第3、4章节我们已经陆续讲完了，唯独除了【response headers】我们还没有讲。

正如【requests headers】存储的是浏览器的请求信息，【response headers】存储的是服务器的响应信息。我们这一章节要找的cookies就在其中。

你会看到在【response headers】里有set cookies的参数。set cookies是什么意思？就是服务器往浏览器写入了cookies。

现在我们就可以谈一谈：cookies究竟是什么？它有什么用？

## cookies及其用法

其实，你对cookies并不陌生，我敢肯定你见过它。比如一般当你登录一个网站，你都会在登录页面看到一个可勾选的选项“记住我”，如果你勾选了，以后你再打开这个网站就会自动登录，这就是cookie在起作用。

当你登录博客账号spiderman，并勾选“记住我”，服务器就会生成一个cookies和spiderman这个账号绑定。接着，它把这个cookies告诉你的浏览器，让浏览器把cookies存储到你的本地电脑。当下一次，浏览器带着cookies访问博客，服务器会知道你是spiderman，你不需要再重复输入账号密码，即可直接访问。

当然，cookies也是有时效性的，过期后就会失效。你应该有过这样的体验：哪怕勾选了“记住我”，但一段时间过去了，网站还是会提示你要重新登录，就是之前的cookies已经失效。

我们继续看【headers】,看看还有没有哪些有关登录的参数。

咦，拉到【form data】，可以看到5个参数：

log和pwd显然是我们的账号和密码，wp-submit猜一下就知道是登录的按钮，redirect_to后面带的链接是我们登录后会跳转到的这个页面网址，testcookie我们不知道是什么。

关于登录的参数我们找到了。现在可以尝试开始写代码，向服务器发起登录请求。
```python
import requests
#引入requests。
url = ' https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
#把登录的网址赋值给url。
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫。
data = {
'log': 'spiderman',  #写入账户
'pwd': 'crawler334566',  #写入密码
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
'testcookie': '1'
}
#把有关登录的参数封装成字典，赋值给data。
login_in = requests.post(url,headers=headers,data=data)
#用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in。
print(login_in)
#打印login_in
```

Response [200]，是返回了200的状态码，意味着服务器接收到并响应了登录请求，我们已经登录成功。

不过，我们的目标是要往博客的文章里发表评论，所以成功登录只是第一步。

怎么发表评论我们现在还不知道。那就先分析看看“正常人”发表评论，浏览器会发送什么请求。

行，我们在《未来已来（一）——技术变革》这篇文章下面自己写一条评论发表（记得不要关闭检查工具，这样才能看到请求的记录）。

我按“正常人”的操作写了一条“纯属测试”的评论，点击发表。

Network里迅速加载出很多请求，点开【wp-comments-post.php】，看headers，发现我刚刚发表的评论就藏在这里。

comment是评论内容，submit是发表评论的按钮，另外两个参数我们看不懂，不过没关系，我们知道它们都是和评论有关的参数就行。

你还会发现【wp-comments-post.php】的数据并没有藏在XHR中，而是放在了Other里。原因是我们搭建网站时就写在了Other里，但常规情况下，大部分网站都会把这样的数据存储在XHR里，比如知乎的回答。

我们想要发表博客评论，首先得登录，其次得提取和调用登录的cookies，然后还需要评论的参数，才能发起评论的请求。

现在，登录的代码我们前面写好了，评论的参数我们刚也找到了，就差提取和调用登录的cookies。

我会先带你写一遍发表评论的代码（要认真看注释）：
```python
import requests
#引入requests。
url = ' https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
#把请求登录的网址赋值给url。
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫。
data = {
'log': 'spiderman',  #写入账户
'pwd': 'crawler334566',  #写入密码
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
'testcookie': '1'
}
#把有关登录的参数封装成字典，赋值给data。
login_in = requests.post(url,headers=headers,data=data)
#用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in。
cookies = login_in.cookies
#提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies。

url_1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
#我们想要评论的文章网址。
data_1 = {
'comment': input('请输入你想要发表的评论：'),
'submit': '发表评论',
'comment_post_ID': '7',
'comment_parent': '0'
}
#把有关评论的参数封装成字典。
comment = requests.post(url_1,headers=headers,data=data_1,cookies=cookies)
#用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment。
#调用cookies的方法就是在post请求中传入cookies=cookies的参数。
print(comment.status_code)
#打印出comment的状态码，若状态码等于200，则证明我们评论成功。
```

提取cookies的方法请看第19的代码：调用requests对象的cookies属性获得登录的cookies。

调用cookies的方法请看第31行的代码：在post请求中传入cookies=cookies的参数。

最后之所以加一行打印状态码的代码，是想运行整个代码后，能立马判断出评论到底有没有成功发表。只要状态码等于200，就说明服务器成功接收并响应了我们的评论请求。

多解释一句：登录的cookies其实包含了很多名称和值，真正能帮助我们发表评论的cookies，只是取了登录cookies中某一小段值而已。所以登录的cookies和评论成功后，你在【wp-comments-post.php】里的headers面板中看到的cookies是不一致的。

总结一下：发表博客评论就三个重点——

### 发表博客评论的三个重点
1. post带着参数请求登录
2. 获得登陆的cookies
3. 带cookies去请求发表评论

虽然我们已经成功发表了评论，但我们的项目到这里还没有结束。因为这个代码还有优化的空间（仅仅是完成还不够，更优雅才是我们该有的追求）。

如果要继续优化这个代码的话，我们需要理解一个新的概念——session（会话）。

## session及其用法

所谓的会话，你可以理解成我们用浏览器上网，到关闭浏览器的这一过程。session是会话过程中，服务器用来记录特定用户会话的信息。

比如你打开浏览器逛购物网页的整个过程中，浏览了哪些商品，在购物车里放了多少件物品，这些记录都会被服务器保存在session中。

如果没有session，可能会出现这样搞笑的情况：你加购了很多商品在购物车，打算结算时，发现购物车空无一物，因为服务器根本没有帮你记录你想买的商品。

对了，session和cookies的关系还非常密切——cookies中存储着session的编码信息，session中又存储了cookies的信息。

当浏览器第一次访问购物网页时，服务器会返回set cookies的字段给浏览器，而浏览器会把cookies保存到本地。

等浏览器第二次访问这个购物网页时，就会带着cookies去请求，而因为cookies里带有会话的编码信息，服务器立马就能辨认出这个用户，同时返回和这个用户相关的特定编码的session。

这也是为什么你每次重新登录购物网站后，你之前在购物车放入的商品并不会消失的原因。因为你在登录时，服务器可以通过浏览器携带的cookies，找到保存了你购物车信息的session。

session的概念，以及和cookies的关系我们搞清楚了，终于可以开始优化发表博客评论的代码。

既然cookies和session的关系如此密切，那我们可不可以通过创建一个session来处理cookies？

不知道。那就翻阅requests的官方文档找找看有没有这样的方法，能让我们创建session来处理cookies。

在requests的高级用法里，还真有这样的方法，太棒了！

优化后的发表评论的代码如下（重点看有注释的代码）：
```python
import requests
#引用requests。
session = requests.session()
#用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies。
url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    'log':input('请输入账号：'), #用input函数填写账号和密码，这样代码更优雅，而不是直接把账号密码填上去。
    'pwd':input('请输入密码：'),
    'wp-submit':'登录',
    'redirect_to':'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
    'testcookie':'1'
}
session.post(url,headers=headers,data=data)
#在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参数。

url_1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
#把我们想要评论的文章网址赋值给url_1。
data_1 = {
'comment': input('请输入你想要发表的评论：'),
'submit': '发表评论',
'comment_post_ID': '7',
'comment_parent': '0'
}
#把有关评论的参数封装成字典。
comment = session.post(url_1,headers=headers,data=data_1)
#在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
print(comment)
#打印comment
```

这么一细看，其实这个代码并没有特别大的优化，我们每次还是需要输入账号密码登录，才能发表评论。

可不可以有更优化的方案？

答案：可以有！cookies能帮我们保存登录的状态，那我们就在第一次登录时把cookies存储下来，等下次登录再把存储的cookies读取出来，这样就不用重复输入账号密码了。

## 存储cookies

我们先把登录的cookies打印出来看看，请点击运行下面的代码（账号：spiderman;密码：crawler334566）。
```python
import requests
session = requests.session()
url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
    'log':input('请输入账号：'),
    'pwd':input('请输入密码：'),
    'wp-submit':'登录',
    'redirect_to':'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
    'testcookie':'1'
}
session.post(url,headers=headers,data=data)
print(type(session.cookies))
#打印cookies的类型,session.cookies就是登录的cookies
print(session.cookies)
#打印cookies
```
执行结果：
```python
<class 'requests.cookies.RequestsCookieJar'>
<RequestsCookieJar[<Cookie 328dab9653f517ceea1f6dfce2255032=87931e7607576f04dcc7c68002783481 for wordpress-edu-3autumn.localprod.forc.work/>, <Cookie wordpress_logged_in_9927dadafec8b913479e6af0fba5e181=spiderman%7C1552490337%7CYoB3qkisr7l18aVw4qmtHDCSw1Wa6j9f4xCnJ0ilzmh%7C6cb6fa031beb18762eae70e5d4ffcb5b92f835c29aeeec3833c4719703a42c3f for wordpress-edu-3autumn.localprod.forc.work/>, <Cookie wordpress_test_cookie=WP+Cookie+check for wordpress-edu-3autumn.localprod.forc.work/>, <Cookie wordpress_sec_9927dadafec8b913479e6af0fba5e181=spiderman%7C1552490337%7CYoB3qkisr7l18aVw4qmtHDCSw1Wa6j9f4xCnJ0ilzmh%7C3c746ef9a55a3133f97f3d3aa147668724b4c2a84da02b3a09bbcf1111b35c6b for wordpress-edu-3autumn.localprod.forc.work/wp-admin>, <Cookie wordpress_sec_9927dadafec8b913479e6af0fba5e181=spiderman%7C1552490337%7CYoB3qkisr7l18aVw4qmtHDCSw1Wa6j9f4xCnJ0ilzmh%7C3c746ef9a55a3133f97f3d3aa147668724b4c2a84da02b3a09bbcf1111b35c6b for wordpress-edu-3autumn.localprod.forc.work/wp-content/plugins>]>
```

RequestsCookieJar是cookies对象的类，cookies本身的内容有点像一个列表，里面又有点像字典的键与值，具体的值我们看不懂，也不需要弄懂。

那怎么把cookies存储下来？能不能用文件读写的方式，把cookies存储成txt文件？

可是txt文件存储的是字符串，刚刚打印出来的cookies并不是字符串。那有没有能把cookies转成字符串的方法？

对了，在第章节关我们知道，json模块能把字典转成字符串。我们或许可以先把cookies转成字典，然后再通过json模块转成字符串。这样，就能用open函数把cookies存储成txt文件。

cookies ----> 字典 --json模块--> 字符串

感觉这样的思路应该可以实现。通过使用搜索引擎+翻阅官方文档的方式，就能找到了把cookies转化成字典的方法和json模块的使用方法。

cookies转换成字典的方法
```python
requests.utils.dict_from_cookiejar(cj)
从CookieJar返回键/值字典
参数：cj-从中提取cookie的CookieJar对象
返回类型：字典
```
json模块的使用方法

JSON函数

使用JSON函数需要导入json库：import json
函数     | 描述    
-------- | --------
json.dumps | 将python对象编码成JSON对象
json.loads | 将已编码的JSON字符串解码为python对象

把cookies存储成txt文件的代码如下（有注释的代码要认真看）：
```python
import requests,json
#引入requests和json模块。
session = requests.session()   
url = ' https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
data = {
'log': input('请输入你的账号:'),
'pwd': input('请输入你的密码:'),
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
'testcookie': '1'
}
session.post(url, headers=headers, data=data)

cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
#把cookies转化成字典。
print(cookies_dict)
#打印cookies_dict
cookies_str = json.dumps(cookies_dict)
#调用json模块的dumps函数，把cookies从字典再转成字符串。
print(cookies_str)
#打印cookies_str
f = open('cookies.txt', 'w')
#创建名为cookies.txt的文件，以写入模式写入内容。
f.write(cookies_str)
#把已经转成字符串的cookies写入文件。
f.close()
#关闭文件。
```
提示：以上存储cookies的方法并非最简单的方法，选取这个方法是因为它容易理解。如果你看完了，请运行代码（账号：spiderman;密码：crawler334566）。

这样一来，cookies的存储我们搞定了，但还得搞定cookies的读取，才能解决每次发表评论都得先输入账号密码的问题。

## 读取cookies

我们存储cookies时，是把它先转成字典，再转成字符串。读取cookies则刚好相反，要先把字符串转成字典，再把字典转成cookies本来的格式。

字符串格式的cookies ----> 字典 --json模块--> cookies

读取cookies的代码如下：
```python
cookies_txt = open('cookies.txt', 'r')
#以reader读取模式，打开名为cookies.txt的文件。
cookies_dict = json.loads(cookies_txt.read())
#调用json模块的loads函数，把字符串转成字典。
cookies = requests.utils.cookiejar_from_dict(cookies_dict)
#把转成字典的cookies再转成cookies本来的格式。
cookies = session.cookies
#获取cookies：就是调用requests对象（session）的cookies属性
```

终于，cookies的存储与读取我们都弄好了。

最后我们可以把代码优化成：如果程序能读取到cookies，就自动登录，发表评论；如果读取不到，就重新输入账号密码登录，再评论。

再一次优化的代码如下：
```python
import requests,json
session = requests.session()
#创建会话。
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#添加请求头，避免被反爬虫。
try:
#如果能读取到cookies文件，执行以下代码，跳过except的代码，不用登录就能发表评论。
    cookies_txt = open('cookies.txt', 'r')
    #以reader读取模式，打开名为cookies.txt的文件。
    cookies_dict = json.loads(cookies_txt.read())
    #调用json模块的loads函数，把字符串转成字典。
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    #把转成字典的cookies再转成cookies本来的格式。
    cookies = session.cookies
    #获取cookies：就是调用requests对象（session）的cookies属性。

except FileNotFoundError:
#如果读取不到cookies文件，程序报“FileNotFoundError”（找不到文件）的错，则执行以下代码，重新登录获取cookies，再评论。

    url = ' https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
    #登录的网址。
    data = {'log': input('请输入你的账号:'),
            'pwd': input('请输入你的密码:'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
            'testcookie': '1'}
    #登录的参数。
    session.post(url, headers=headers, data=data)
    #在会话下，用post发起登录请求。

    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    #把cookies转化成字典。
    cookies_str = json.dumps(cookies_dict)
    #调用json模块的dump函数，把cookies从字典再转成字符串。
    f = open('cookies.txt', 'w')
    #创建名为cookies.txt的文件，以写入模式写入内容
    f.write(cookies_str)
    #把已经转成字符串的cookies写入文件
    f.close()
    #关闭文件

url_1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
#文章的网址。
data_1 = {
'comment': input('请输入你想评论的内容：'),
'submit': '发表评论',
'comment_post_ID': '7',
'comment_parent': '0'
}
#评论的参数。
comment = session.post(url_1,headers=headers,data=data_1)
#在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment。
print(comment.status_code)
#打印comment的状态码
```

这样是解决了每一次都要重复输入账号密码的问题，但这个代码还存在一个缺陷——并没有解决cookies会过期的问题。

cookies是否过期，我们可以通过最后的状态码是否等于200来判断。但更好的解决方法应该在代码里加一个条件判断，如果cookies过期，就重新获取新的cookies。

所以，更完整以及面向对象的代码应该是下面这样的：
```python
import requests, json
session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def cookies_read():
    cookies_txt = open('cookies.txt', 'r')
    cookies_dict = json.loads(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return (cookies)
    # 以上4行代码，是cookies读取。

def sign_in():
    url = ' https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
    data = {'log': input('请输入你的账号'),
            'pwd': input('请输入你的密码'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
            'testcookie': '1'}
    session.post(url, headers=headers, data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    f = open('cookies.txt', 'w')
    f.write(cookies_str)
    f.close()
    # 以上5行代码，是cookies存储。


def write_message():
    url_2 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
    data_2 = {
        'comment': input('请输入你要发表的评论：'),
        'submit': '发表评论',
        'comment_post_ID': '7',
        'comment_parent': '0'
    }
    return (session.post(url_2, headers=headers, data=data_2))
    #以上9行代码，是发表评论。

try:
    session.cookies = cookies_read()
except FileNotFoundError:
    sign_in()
    session.cookies = cookies_read()

num = write_message()
if num.status_code == 200:
    print('成功啦！')
else:
    sign_in()
    session.cookies = cookies_read()
    num = write_message()
```

