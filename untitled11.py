#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:20:29 2019

@author: user
"""

entity_list = []

for doc_name in glob.glob("*.xml"):
    path = "/home/user/Desktop/folia_docs/"
    doc = folia.Document(file=doc_name)
    with open(path + doc_name, "w+") as f:
        for i,sentence in enumerate(doc.sentences()):
            for layer in sentence.select(folia.EntitiesLayer):
                for entity in layer.select(folia.Entity):
                    entity_list.append(entity.cls)