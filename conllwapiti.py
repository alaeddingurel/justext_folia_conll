#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:34:01 2019

@author: user
"""

with open("/home/user/Desktop/conll_folia_file/conlltry") as f:
    content = f.read()
    
content = content.replace("ORG","O")
content = content.replace("PER","O")
    
with open('/home/user/Desktop/conll_folia_file/conlltry', 'w') as file:
  file.write(content)
  
  
  
with open("/home/user/Desktop/conll_folia_file/conlltry_labels") as f:
    content = f.readlines()

content = [x.strip() for x in content]

found_num = 0
not_found = 0
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
    
  
# FOUND LOC
# /home/user/Desktop/wapiti-1.5.0/wapiti train -a sgd-l1 -p Pattern -2 20 conlltry model

    
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