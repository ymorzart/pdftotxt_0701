# -*- coding: utf-8 -*-

"""
Created on Tue Jul 01 14:03:06 2020

@author: vincent.yu

Download Web Site PDF file 
SDS HomePage Download SDS Sustainability Report 2020
"""
import os

import requests
import shutil

#res = requests.get('http://journals.sagepub.com/doi/pdf/10.1038/jcbfm.1993.48', stream=True, verify=False)
#res = requests.get('https://image.samsungsds.com/global/en/gnb/about/__icsFiles/afieldfile/2020/06/25/SamsungSDS_Sustainability_Report_2020_en_f.pdf?queryString=20200630070452', stream=True, verify=False)
res = requests.get('https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200705-covid-19-sitrep-167.pdf?sfvrsn=17e7e3df_2',stream=True, verify=False)
with open('K:/My files/Download/wordCloud/pdftotxt/abcd.pdf', 'wb') as f:
    res.raw.decode_content = True
    shutil.copyfileobj(res.raw, f)
