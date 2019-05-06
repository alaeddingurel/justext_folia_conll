#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:04:33 2019

@author: user
"""

import glob
import subprocess
import sys

justext_file_dir = sys.argv[1]
output_dir = sys.argv[2]

# JUSTEXT TO TEXT FILES TO FOLIA XML FILES
for doc_name in glob.glob("*.txt"):
    real = doc_name[:-4]
    folia_name = real + ".folia.xml"
    """ path = "/home/user/Desktop/justext_folia_extended/"
    save_path = "/home/user/Desktop/justext_folia_extended_tofolia/" """
    command = "ucto -L eng " + justext_file_dir + doc_name + " " + output_dir + folia_name
    
    print(command)
    subprocess.Popen(command.split(), stdout=subprocess.PIPE)
