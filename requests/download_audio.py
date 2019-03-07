# 音频下载
import requests

res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

music = res.content

mp3 = open('over_the_rainbow.mp3','wb')

mp3.write(music)

mp3.close()