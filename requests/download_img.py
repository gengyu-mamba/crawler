# 图像下载
import requests

res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')

picture = res.content

photo = open('ppt.png', 'wb')

photo.write(picture)

photo.close()