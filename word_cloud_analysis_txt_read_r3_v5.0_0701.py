# -*- coding: utf-8 -*-
"""
Created on Tue Jul 01 15:03:06 2020

@author: vincent.yu

Word Cloud Analysis Eng Ver 5.0
Input Text file and analysis Word Cloud 
"""
import os
os.environ["HTTP_PROXY"] = "http://70.10.15.10:8080"
os.environ["HTTPS_PROXY"] = "http://70.10.15.10:8080"
os.environ["PYTHONHTTPSVERIFY"] = "0"

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime
from bs4 import BeautifulSoup 
import time 
from datetime import datetime
import requests


datestring = datetime.strftime(datetime.now(),'%Y_%m_%d_%H_%M')
#현 작업 디렉토리
print("현재 폴더: ", os.getcwd())
# 디렉토리 변경 
os.chdir("K:/My files/Download/wordCloud/pdftotxt")
print("변경 폴더: ", os.getcwd())

##별도 작성된 영문자료 읽어서 분석 할때 사용## 
file_name = str(input("분석할 화일명을 입력하세요:"))
text = open(file_name,encoding='utf-8').read()

#text 입력변수 분석
wordcloud = WordCloud(background_color='white',
                       width = 1920,
                       height = 1080).generate(text)
fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear',cmap='YlOrBr')
plt.axis('off')

plt.savefig('K:/My files/Download/wordCloud/Word_'+ datestring +'.png')

