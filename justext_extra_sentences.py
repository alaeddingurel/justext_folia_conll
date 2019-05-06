#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:59:47 2019

@author: user
"""

import glob


with open("/home/user/Desktop/justext_folia/https__timesofindia.indiatimes.com_city_ahmedabad_11-SIMI-activists-held-in-city_articleshow_298322426.folia.xml", "r") as f:
    content = f.read()
    
separator = "All Comments ()+^ Back to Top"

head, sep, tail = content.partition(separator)


# EXTRACT NEWS
for filename in glob.glob("*.xml"):
    path = "/home/user/Desktop/justext_folia/"
    wri_path = "/home/user/Desktop/justext_folia_extended/"
    ext_path = path + filename
    wri_ext_path = wri_path + filename
    with open(ext_path, "r") as f:
        content = f.read()
        head, sep, tail = content.partition(separator)
        with open(wri_ext_path, "w") as g:
            g.write(head)



# RENAME FILES FOR UCTO AS .TXT
import os
            
for filename in glob.glob("*"):
    wri_path = "/home/user/Desktop/justext_folia_extended/"
    wri_ext_path = wri_path + filename
    to_change_filename = wri_ext_path + ".txt"
    os.rename(wri_ext_path, to_change_filename)
    