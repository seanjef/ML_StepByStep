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
Y=dataset.iloc[:,3].values  #python start index from 0

#taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")  #在Imputer後ctrl+i 在spyder就會出現helper documents 
imputer = imputer.fit(X[:,1:3])  #針對數值欄位利用欄位特徵值取平均數做遺漏值取代 
X[:,1:3] = imputer.transform(X[:,1:3])

   