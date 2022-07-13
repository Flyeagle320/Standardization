# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importing packages 
import pandas as pd

#importing Dataset seedsdata##
seeds = pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/DataSets-Data Pre Processing/DataSets/Seeds_data.csv')

seeds.info()
##there are no null value##

seeds.describe() ##to find mean , median , IQR ##

EDA =pd.DataFrame({'columns_name': [seeds.columns],
                   'means': [seeds.mean()],
                   'median': [seeds.median()],
                   'mode': [seeds.mode()],
                   'std dev': [seeds.std()],
                   'var':[seeds.var()],
                   'skew': [seeds.skew()],
                   'kurtosis':[seeds.kurt()]})
EDA

import matplotlib.pyplot as plt

##lets find outlier in the data##
##using boxplot for every column##
for column in seeds:
    plt.figure()
    seeds.boxplot([column])

seeds.columns    
    
#we have outliers in Compactness and Assymetry_coeff##
boxplot = seeds.boxplot(column=['Area', 'Perimeter ', 'Compactness', 'length', 'Width',
       'Assymetry_coeff', 'len_ker_grove', 'Type'])    

##Standardization funct using Z std 
def norm_func(i):
    x=(i-i.mean(i))/(i.std(i))
    return(x)

##standardization data frame (considering numerical part of data frame)
seeds_norm =pd.DataFrame(seeds.iloc[:,0:7])
seeds_norm.describe()


