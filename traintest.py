#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:04:49 2019

@author: user
"""

# ORG, PER
with open("/home/user/Desktop/conll_folia_file/folia_train") as f:
    content = f.read()
    
content = content.replace("ORG","O")
content = content.replace("PER","O")

with open('/home/user/Desktop/conll_folia_file/folia_train', 'w') as file:
  file.write(content)
  

with open("/home/user/Desktop/conll_folia_file/folia_test") as f:
    content = f.read()
    
content = content.replace("ORG","O")
content = content.replace("PER","O")

with open('/home/user/Desktop/conll_folia_file/folia_test', 'w') as file:
  file.write(content)
    




total_loc = 0

# TOTAL_LOC

with open("/home/user/Desktop/conll_folia_file/folia_test_new.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

    
for loc in content:
    
    try:
        splitted_loc = loc.split()[1]
        if splitted_loc == "LOC":
            total_loc = total_loc + 1
    except:
        continue



found_num = 0
not_found = 0

with open("/home/user/Desktop/conll_folia_file/folia_test_new.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
    
for i in content:
    splitted = i.split("\t")
    
    try:
        if splitted[0].split()[1] == "LOC" and splitted[1] == "LOC" :
            found_num = found_num + 1
        else:
            not_found = not_found + 1
    except:
        continue