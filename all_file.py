#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:57:41 2019

@author: user
"""

import glob

with open('/home/user/Desktop/all.txt', 'w') as outfile:
    for fname in glob.glob("*.xml"):
        with open(fname) as infile:
            outfile.write(infile.read())
            

