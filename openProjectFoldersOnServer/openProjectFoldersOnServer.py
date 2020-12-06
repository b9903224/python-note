# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 00:01:38 2020

@author: b9903

https://www.w3resource.com/python-exercises/os/python-os-exercise-2.php
"""

import os
import time

## 定義位置
projectParentPath = r'D:\backup\20201206\project'
destFolders = ['', 'source_code', 'test_file']

## 建立project name序列
folders = os.listdir(projectParentPath)
projectNames = [ name for name in folders if os.path.isdir(os.path.join(projectParentPath, name)) ]

#projectNameMap = {index+1:projectName for index, projectName in enumerate(projectNames)}
projectNameMap = {}
for index, projectName in enumerate(projectNames):
    print('[%g] %s'%(index+1, projectName))
    projectNameMap[index+1] = projectName

## 使用者輸入要哪個project
while True:
    projectIndex = int(input("請輸入project index: "))
    if projectIndex in projectNameMap:
        break
    else:
        print('找不到project index')

## 打開資料夾
projectName = projectNameMap[projectIndex]
projectPath = os.path.join(projectParentPath, projectName)
for destFolder in destFolders:
    os.startfile(os.path.join(projectPath, destFolder))
    time.sleep(0.5)















