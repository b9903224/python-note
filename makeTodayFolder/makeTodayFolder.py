# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:50:44 2020

@author: b9903
"""

import os
from datetime import datetime

pwd = os.getcwd()

now = datetime.now() # current date and time
dateFolder = now.strftime("%Y%m%d")

datePath = os.path.join(pwd, dateFolder)
#aaa
print('Make folder for %s'%datePath)

os.makedirs(dateFolder)

