#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 10:23:22 2019

@author: user
"""

import pandas as pd


df = pd.read_fwf('/home/user/Desktop/all_info.csv')

df = df['gandhi bhavan']


from pynlpl.formats import folia

for doc_name in glob.glob("*.xml"):
    df = pd.read_fwf('/home/user/Desktop/new_partial_folia_file/' + doc_name , header=None)
    series = []
    for elem in df[0]:
        new = re.split(r'\t+', elem)
        if len(new) > 1:
            series.append(elem)
#        print(len(series))
    df_ne = pd.DataFrame(series, columns=['text'])
    print(doc_name)
    print("Unique number" + str(len(df_ne.text.unique())))
    duplicate = df_ne[df_ne.text.duplicated()]
    print("Duplication number : " + str(len(duplicate)))
    
    

doc = folia.Document(file=filename)

doc.text()