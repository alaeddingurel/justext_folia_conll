#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:51:14 2019

@author: user
"""

import justext
import requests
import re
import glob

from collections import Counter

response = requests.get("https://timesofindia.indiatimes.com/city/ahmedabad/Amarsinh-who-Congress-what/articleshow/1746346645.cms")

# Folia Docslar için link üretmek vb.
file_link = {}
for file in glob.glob("*.xml"):
    link = file.replace("__", "://")
    link = link.replace("_", "/")
    link = link.replace(".folia.xml", ".cms")
    print(link)
    file_link[file] = link
    
path_just = '/home/user/Desktop/justext_folia/'
path_part = '/home/user/Desktop/new_partial_folia_file/'


# Linklerin html dosyalarından textleri çekip dosyaya yazdırıyor
for file in file_link.keys():
    response = requests.get(file_link[file])
    with open(path_just+file, "w+") as f:
        paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
        for paragraph in paragraphs:
          if not paragraph.is_boilerplate:
            print (paragraph.text)
            f.write(paragraph.text+"\n")
        f.close()
        
found = 0
not_found = 0
count_list_found = []
count_list_not_found = [] 


for file in file_link.keys():
    f = open(path_just+file, "r")
    text = f.read()
    with open(path_part+file, "r") as a:
        content = a.readlines()
    print(file)
        
    tab_list = []
    
#    for i in tab[0].split():
#        reg_str = reg_str + i + "\W*"
#    reg_str = reg_str[:-3]
#    print(reg_str)
    
    
    for cont in content:
        tab = re.split(r'\t+', cont)
        tab_list.append(tab)
        
    for tab in tab_list:
        reg_str = ""
        for i in tab[0].split():
            reg_str = reg_str + re.escape(i) + "\W*"
        reg_str = reg_str[:-3]
        print(reg_str)
        if re.search(reg_str, text):
            found = found + 1
            count_list_found.append(tab[1])
            
        else:
            not_found = not_found + 1
            print("Not Found" + tab[1])
            print(text)
            count_list_not_found.append(tab[1])