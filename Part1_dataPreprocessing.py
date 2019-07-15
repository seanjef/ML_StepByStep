# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir('D:\\AI_Docs\\Udemy\\ML_A-Z\\Machine Learning A-Z Template Folder\\Part 1 - Data Preprocessing\\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\\')
dataset = pd.read_csv('Data.csv')
dataset.head()

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values

