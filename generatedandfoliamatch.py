#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 12:52:00 2019

@author: user
"""
import sys
import glob
from pynlpl.formats import folia

def indices(l, val):
    """Always returns a list containing the indices of val in the_list"""
    return [index for index, value in enumerate(l) if value == val]

path = "/home/user/Desktop/foexample.folia.xml"
doc = folia.Document(file=path)
with open("/home/user/Desktop/foexamplecon.txt", "w") as f:
    for i,sentence in enumerate(doc.sentences()):
        for word in sentence:
            f.write(word.text() + "\n")
            
            
with open("/home/user/Desktop/new_partial_folia_file_extended/https__timesofindia.indiatimes.com_city_ahmedabad_11-SIMI-activists-held-in-city_articleshow_298322426.folia.xml") as f:
    content = f.readlines()

content = [x.strip() for x in content]

doc = "https__timesofindia.indiatimes.com_city_ahmedabad_11-SIMI-activists-held-in-city_articleshow_298322426.txt"
with open("/home/user/Desktop/justext_folia_extended_tofolia_toconll/" + doc) as f:
    o_content = f.readlines()
    
o_content = [x.strip() for x in o_content]


# Generateed match with ucto tokenized justext news

is_match = []


full_list = []


for elem in content:
    text = elem.split("\t")[0]
    first_word = text.split()[0]
#    print(elem.split()[0])
    for i in indices(o_content, first_word):
        print(i)
        index = i
        count_list = []
        a = iter(text.split())
        for b in range(len(text.split())):
            count = 0
            if o_content[index] == next(a):
                index = index + 1
                count = count + 1
            else:
                count_list.append(count)
        full_list.append(count_list)
        
        
        
# Trying indices



all_list = []

for elem in content:
    text = elem.split("\t")[0]
    first_word = text.split()[0]
    count_ind_list = []
    for i in indices(o_content, first_word):
        index = i
        count = 0
        for b in range(len(text.split())):
            print(indices(o_content, first_word))
            print(index)
            print(o_content[index])
            if (o_content[index+b] == text.split()[b]):
                continue
            else:
                count_ind_list.append(count)
                break
            count_ind_list.append(count)
            print("-------------------------------------")

    all_list.append(count_ind_list)
        
text = content[0].split("\t")[0]
first_word = text.split()[0]


tag_list = ["etype","pname","fname","etime","place"]

whitespace_indice = indices(o_content, "")
spac_o_content = list(filter(None, o_content)) # Remove empty strings
spac_o_content_splitted = [cont.split() for cont in spac_o_content]
spac_token = [row.split()[0] for row in spac_o_content]
all_list = []
for elem in content:
    text = elem.split("\t")[0]
    tag = elem.split("\t")[1]
    first_word = text.split()[0]
#    print(tag)
    
    count_list = []

    indice = indices(spac_token, first_word)
    for i in indice:
        count = 0
        for x in range(len(text.split())):
            index = x
#            print(o_content[i+x])
#            print(text.split()[x])
            if i+x >= len(spac_token):
                break
            if spac_token[i+x] == text.split()[x]:
                count = count + 1
#                print("True")
            else:
                continue
#                print("False")
        count_list.append(count)
    
    which_index = indice[count_list.index(max(count_list))]+1
    to_index = which_index + len(text.split())-2
    if tag in tag_list:
        print(tag)
        for b in range(which_index, to_index):
            print("in")
            print(str(which_index) + "," + str(to_index))
            spac_o_content_splitted[b][1] = tag
            print(spac_o_content_splitted[b][1])
            
            
        
    
#    print(indice[count_list.index(max(count_list))])    
#    print(tag)
#    print(count_list.index(max(count_list)))
    all_list.append(count_list)

for i in whitespace_indice:
    spac_o_content_splitted.insert(i, "")
