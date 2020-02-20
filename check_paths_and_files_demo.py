# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:54:26 2020

@author: b9903

"""

import os

def check_paths_and_files(*paths):
    current_path = os.getcwd()
    files = os.listdir(current_path)
    
    print('current path: "%s"'%(current_path))
    print('current path dir & files: %g'%(len(files)))
    print(files)
    print('*'*20)
    for path in paths:
        if not os.path.exists(path):
            print('"%s" not exists'%(path))
        elif os.path.isdir(path):
            files = os.listdir(path)
            print('path: "%s"'%(path))
            print('dir & files: %g'%(len(files)))
            print(files)
        elif os.path.isfile(path):
            print('file exist: "%s"'%(path))
        else:
            print('undefined: "%s"'%(path))
        print('-'*20)
    print()
    print()

check_paths_and_files()
check_paths_and_files('multiprocessing_1.py', 'utility', '.\demo', './demo', r'D:\Users\b9903\Desktop\Git\python-utility', 'abc', '.123')