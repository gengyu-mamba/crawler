# CSV&Excel

上一章节，我们主要学习了如何带参数地请求数据（get请求）和Request Headers的用法，最终爬取到了想要的数据。

那么有一个新的问题来了——爬到的数据要怎么存下来？

可能你会想到这样的方案：把爬到的数据一条条复制黏贴，然后存成Excel文件。这样的方案对于存储十几条数据还好说，可是当我们爬取到的数据超过几百条时，这样的方案显然不可取。

到了这一章节，获取数据、解析数据以及提取数据，我们都学会了。唯独差了存储数据这一步，这也是整个爬虫过程中不可或缺的一步。

所以，这一关要讲解的核心内容就是存储数据的正确方式。

## 存储数据的方式

其实，常用的存储数据的方式有两种——存储成csv格式文件、存储成Excel文件（不是复制黏贴的那种）。

我猜想，此时你会想问“csv”是什么，和Excel文件有什么区别？

前面，我有讲到json是特殊的字符串。其实，csv也是一种字符串文件的格式，它组织数据的语法就是在字符串之间加分隔符——行与行之间是加换行符，同列之间是加逗号分隔。

它可以用任意的文本编辑器打开（如记事本），也可以用Excel打开，还可以通过Excel把文件另存为csv格式（因为Excel支持csv格式文件）。

运行以下三行代码，你就能直观清晰地知道csv是什么。
```python
file=open('test.csv','a+')
#创建test.csv文件，以追加的读写模式
file.write('海王,神探蒲松龄,复仇者联盟4')
#写入test.csv文件
file.close()
#关闭文件
```

将我们刚刚写入的csv文件下载到本地电脑，再用记事本打开，你会看到：
![csv](https://github.com/gengyu-mamba/python-crawler/blob/master/resource/csv.png)

用Excel打开，则是这样的：
![excel](https://github.com/gengyu-mamba/python-crawler/blob/master/resource/excel.png)

发现了吗？csv文件里的逗号可以充当分隔同列字符串的作用。

为什么要加分隔符？因为不加的话，数据都堆在一起，会显得杂乱无章，也不方便我们之后提取和查找。这也是一种让数据变得有规律的组织方式。

另外，用csv格式存储数据，读写比较方便，易于实现，文件也会比Excel文件小。但csv文件缺少Excel文件本身的很多功能，比如不能嵌入图像和图表，不能生成公式。

至于Excel文件，不用我多说你也知道就是电子表格。它有专门保存文件的格式，即xls和xlsx（Excel2003版本的文件格式是xls，Excel2007及之后的版本的文件格式就是xlsx）。

好啦，csv和Excel文件你都清楚了，我们可以继续学习存储数据的基础知识——如何写入与读取csv格式文件和Excel文件的数据。

## 存储数据的基础知识

存储成csv格式文件和存储成Excel文件，这两种不同的存储方式需要引用的模块也是不同的。操作csv文件我们需要借助csv模块；操作Excel文件则需要借助openpyxl模块。

### 基础知识：csv写入与读取

好。现在请你跟着我的节奏，我们一起先搞清楚如何往csv格式文件写入数据。

首先，我们要引用csv模块。因为Python自带了csv模块，所以我们不需要安装就能引用它。

你是不是会困惑，明明前面csv写入我们可以直接用open函数来写，为什么现在还要先引用csv模块？答案：直接运用别人写好的模块，比我们使用open()函数来读写，语法更简洁，功能更强大，待会你就能感受到。那么，何乐而不为？
```python
import csv
#引用csv模块。
csv_file = open('demo.csv','w',newline='')
#创建csv文件，我们要先调用open()函数，传入参数：文件名“demo.csv”、写入模式“w”、newline=''。
```

然后，我们得创建一个新的csv文件，命名为“demo.csv”。

“w”就是writer，即文件写入模式，它会以覆盖原内容的形式写入新添加的内容。

加newline=' '参数的原因是，可以避免csv文件出现两倍的行距（就是能避免表格的行与行之间出现空白行）。

创建完csv文件后，我们要借助csv.writer()函数来建立一个writer对象。
```python
import csv
#引用csv模块。
csv_file = open('demo.csv','w',newline='')
#调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''。
writer = csv.writer(csv_file)
# 用csv.writer()函数创建一个writer对象。
```

那怎么往csv文件里写入新的内容呢？答案是——调用writer对象的writerow()方法。

writer.writerow(['电影','淘票票评分'])
#借助writerow()函数可以在csv文件里写入一行文字 "电影"和“淘票票评分”。

提醒：writerow()函数里，需要放入列表参数，所以我们得把要写入的内容写成列表。就像['电影','淘票票评分']。

我们试着再写入两部电影的名字和其对应的豆瓣评分，最后关闭文件，就完成csv文件的写入了。
```python
import csv
#引用csv模块。
csv_file = open('demo.csv','w',newline='')
#调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''。
writer = csv.writer(csv_file)
# 用csv.writer()函数创建一个writer对象。
writer.writerow(['电影','淘票票评分'])
#调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “电影”和“淘票票评分”。
writer.writerow(['惊奇队长','8.6'])
#在csv文件里写入一行文字 “惊奇队长”和“8.6”。
writer.writerow(['绿皮书','9.4'])
#在csv文件里写入一行文字 “绿皮书”和“9.4”。
csv_file.close()
#写入完成后，关闭文件就大功告成啦！
```

运行代码后，名为“demo.csv”的文件会被创建。用Excel或记事本打开这个文件，你就能看到——
![csv](https://github.com/gengyu-mamba/python-crawler/blob/master/resource/demo_csv.png)

![excel](https://github.com/gengyu-mamba/python-crawler/blob/master/resource/demo_excel.png)

### 基础知识：Excel写入与读取
在开始讲Excel文件的写入与读取前，我们还得稍微了解一下Excel文档的基本概念。

一个Excel文档也称为一个工作薄（workbook），每个工作薄里可以有多个工作表（wordsheet），当前打开的工作表又叫活动表。

每个工作表里有行和列，特定的行与列相交的方格称为单元格（cell）。比如上图第A列和第1行相交的方格我们可以直接表示为A1单元格。

清楚了Excel的基础概念，我们可以来说下openpyxl模块是怎么操作Excel文件的了。照例先说写入后说读取。

#### openpyxl的安装

要安装 openpyxl，Windows用户只要在你的终端中运行这个简单命令即可：
```python
pip install openpyxl
```
Mac用户只要在你的终端中运行这个简单命令即可：
```python
pip3 install openpyxl
```
装好openpyxl模块后，首先要引用它，然后通过openpyxl.Workbook()函数就可以创建新的工作薄，代码如下：
```python
import openpyxl 
#引用openpyxl 。
wb = openpyxl.Workbook()
#利用openpyxl.Workbook()函数创建新的workbook（工作薄）对象，就是创建新的空的Excel文件。
```

创建完新的工作薄后，还得获取工作表。不然程序会懵逼，不知道要把内容写入哪张工作表里。
```python
sheet = wb.active
#wb.active就是获取这个工作薄的活动表，通常就是第一个工作表。
sheet.title = 'new title'
#可以用.title给工作表重命名。现在第一个工作表的名称就会由原来默认的“sheet1”改为"new title"。
```

添加完工作表，我们就能来操作单元格，往单元格里写入内容。
```python
sheet['A1'] = '西游记' 
#把'西游记'赋值给第一个工作表的A1单元格，就是往A1的单元格中写入了'西游记'。
```

往单元格里写入内容只要定位到具体的单元格，如A1（根据Excel的坐标，A1代表第一列第一行相交的单元格），然后给这个单元格赋值即可。

如果我们想往工作表里写入一行内容的话，就得用到append函数。
```python
row = ['孙悟空','猪八戒','沙悟净']
#把我们想写入的一行内容写成列表，赋值给row。
sheet.append(row)
#用sheet.append()就能往表格里添加这一行文字。
```

如果我们想要一次性写入的不止一行，而是多行内容，又该怎么办？代码如下：
```python
rows = [['孙悟空','猪八戒','沙悟净'],['是','四大','名著', '经典','人物']]
#先把要写入的多行内容写成列表，再放进大列表里，赋值给rows。
for i in rows:
    sheet.append(i)
#遍历rows，同时把遍历的内容添加到表格里，这样就实现了多行写入。
print(rows)
#打印rows
```
成功写入后，我们千万要记得保存这个Excel文件，不然就白写啦！
```python
wb.save('west.xlsx')
#保存新建的Excel文件，并命名为“west.xlsx”
```

这样，Excel文件写入的代码我们就写好了，可以运行一下代码。
```python
import openpyxl 
wb=openpyxl.Workbook() 
sheet=wb.active
sheet.title='new title'
sheet['A1'] = '西游记'
rows= [['孙悟空','猪八戒','沙悟净'],['是','四大','名著', '经典','人物']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('west.xlsx')
```

下面，我们来搞定存储数据最后的一个基础知识点——Excel文件的读取。

一行行来看这个读取Excel文件的代码：
```python
import openpyxl 
#写入的代码：
wb=openpyxl.Workbook() 
sheet=wb.active
sheet.title='new title'
sheet['A1'] = '西游记'
rows= [['孙悟空','猪八戒','沙悟净'],['是','四大','名著', '经典','人物']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('west.xlsx')

#读取的代码：
wb = openpyxl.load_workbook('west.xlsx')
sheet = wb['new title']
sheetname = wb.sheetnames
print(sheetname)
A1_cell = sheet['A1']
A1_value = A1_cell.value
print(A1_value)
```
第14行代码：调用openpyxl.load_workbook()函数，打开“west.xlsx”文件。

第15行代码：获取“west.xlsx”工作薄中名为“new title”的工作表。

第16、17行代码：sheetnames是用来获取工作薄所有工作表的名字的。如果你不知道工作薄到底有几个工作表，就可以把工作表的名字都打印出来。

第18-20行代码：把“new title”工作表中A1单元格赋值给A1_cell，再利用单元格value属性，就能打印出A1单元格的值。

学会Excel写入后，读取Excel还是比较简单的对吧？

如果你对openpyxl模块感兴趣，想要有更深入的了解的话，推荐阅读openpyxl模块的官方文档：https://openpyxl.readthedocs.io/en/stable/






