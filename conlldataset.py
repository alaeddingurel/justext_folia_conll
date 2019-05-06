#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:31:53 2019

@author: user
"""
# CONLL TEST DATASET
with open("/home/user/Desktop/ConllOri/test.txt") as f:
    g = open("/home/user/Desktop/ConllOri/new_test.txt", "w")
    for line in f:
        line = line.split()
        if not line:
            g.write("\n")
        else:
            try:
                g.write(line[0] + " " + line[3] + "\n")
            except:
                pass            
        

with open("/home/user/Desktop/ConllOri/new_test.txt") as f:
    content = f.read()

content = content.replace("I-LOC","LOC")
content = content.replace("B-LOC","LOC")
content = content.replace("I-PER","O")
content = content.replace("B-PER","O")
content = content.replace("I-MISC","O")
content = content.replace("B-MISC","O")

with open("/home/user/Desktop/ConllOri/new_test.txt" , "w") as file:
    file.write(content)
    
    
# CONLL TRAIN DATASET   
with open("/home/user/Desktop/ConllOri/train.txt") as f:
    g = open("/home/user/Desktop/ConllOri/new_train.txt", "w")
    for line in f:
        line = line.split()
        if not line:
            g.write("\n")
        else:
            try:
                g.write(line[0] + " " + line[3] + "\n")
            except:
                pass            
        

with open("/home/user/Desktop/ConllOri/new_train.txt") as f:
    content = f.read()

content = content.replace("I-LOC","LOC")
content = content.replace("B-LOC","LOC")
content = content.replace("I-PER","O")
content = content.replace("B-PER","O")
content = content.replace("I-MISC","O")
content = content.replace("B-MISC","O")
content = content.replace("I-ORG", "O")
content = content.replace("B-ORG", "O")

with open("/home/user/Desktop/ConllOri/new_train.txt" , "w") as file:
    file.write(content)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# TOTAL LOC
   
total_loc = 0

with open("/home/user/Desktop/conll_folia_file/new_test_new.txt") as f:
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

found_num = 0
not_found = 0

with open("/home/user/Desktop/conll_folia_file/new_test_new.txt") as f:
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