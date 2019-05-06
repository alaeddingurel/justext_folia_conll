#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:02:10 2019

@author: user
"""
import re
from pynlpl.formats import folia
import glob

def getwordtext(entity):
    annot = ""
    for word in entity.wrefs():
        annot = annot + word.text()
        if word.space:
            annot = annot + " "
    return annot

for doc_name in glob.glob("*.xml"):
    path = "/home/user/Desktop/try_folia/"
    doc = folia.Document(file=doc_name)
    path = path + doc_name
    with open(path, "w+") as f:
        for i,sentence in enumerate(doc.sentences()):
                for layer in sentence.select(folia.EntitiesLayer):
                    for entity in layer.select(folia.Entity):
        
                        
                        annot = getwordtext(entity)
                        #annot = " ".join([word.text() for word in entity.wrefs()])
                        try:
                            jkl = re.search(r"w\.(\d+)$", entity.wrefs()[0].id)
                            prev = doc[re.sub(r"(.*w\.)\d+$", r"\g<1>" + str(int(jkl.group(1)) - 1), entity.wrefs()[0].id)]
                            annot = prev.text() + "\t" + annot
                            print(annot)
                        except:
                            #print("No prev " + re.search(r"w\.(\d+)$", entity.wrefs()[0].id).group(1))
                            gfg = 0
        
                        try:
                            after = re.search(r"w\.(\d+)$", entity.wrefs()[-1].id)
                            after = doc[re.sub(r"(w\.)\d+$", r"\g<1>" + str(int(after.group(1)) + 1), entity.wrefs()[0].id)]
                            annot = annot + after.text()
                            annot = annot + "\t" + entity.cls
                            print(annot)
                            f.write(annot + "\n")
                        except:
                            #print("No after " + entity.wrefs()[0].id)
                            gfg = 0