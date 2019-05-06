#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:16:59 2019

@author: user
"""

import subprocess


# JUSTEXT TO TEXT FILES TO FOLIA XML FILES
for doc_name in glob.glob("*.txt"):
    real = doc_name[:-4]
    folia_name = real + ".folia.xml"
    path = "/home/user/Desktop/justext_folia_extended/"
    save_path = "/home/user/Desktop/justext_folia_extended_tofolia/"
    command = "ucto -L eng " + path + doc_name + " " + save_path + folia_name
    
    print(command)
    subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    
    
# FOLIA XML FILES TO CONLL FORMAT FILE
    
for doc_name in glob.glob("*.xml"):
    path = "/home/user/Desktop/justext_folia_extended_tofolia_toconll/"
    doc = folia.Document(file=doc_name)
    real = doc_name[:-10]
    path = path + real + ".txt"
    with open(path, "w+") as f:
        for i,sentence in enumerate(doc.sentences()):
            for word in sentence:
                f.write(word.text() + " O" +"\n")
            f.write("\n")
                