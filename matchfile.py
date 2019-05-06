#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:06:39 2019

@author: user
"""
import glob

def indices(l, val):
    """Always returns a list containing the indices of val in the_list"""
    return [index for index, value in enumerate(l) if value == val]




for file in glob.glob("*.xml"):

    with open("/home/user/Desktop/new_partial_folia_file_extended/" + file) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]
    
    doc = file[:-10] + ".txt"
    with open("/home/user/Desktop/justext_folia_extended_tofolia_toconll/" + doc) as f:
        o_content = f.readlines()
        
    o_content = [x.strip() for x in o_content]


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