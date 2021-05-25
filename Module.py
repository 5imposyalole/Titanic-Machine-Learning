#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import Module
import math
import importlib
importlib.reload(Module)
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import lecture12util as lu
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


def calc(df):
    #Remove unnecessary data and filter 
    df = df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'])
    df = df[df['Embarked'].notna()]
    df = df[df['Age'].notna()]
    arr = df.to_numpy()
    counter = len(arr[0,:])
    le = preprocessing.LabelEncoder()
    
    for i in range(counter):
        if any(isinstance(x, str) for x in arr[:,i]):
            arr[:,i] = le.fit_transform(arr[:,i])

    return  arr            


def calc_survive_male(df):
    #Remove unnecessary data and filter
    df = df.loc[(df['Survived'] == 1) & (df['Sex'] == 'male')] 
    df = df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'])
    df = df[df['Embarked'].notna()]
    df = df[df['Age'].notna()]
    #df1 = df.loc[(df['Sex'] == 'female')] 

    arr = df.to_numpy()
    counter = len(arr[0,:])
    le = preprocessing.LabelEncoder()
    
    for i in range(counter):
        if any(isinstance(x, str) for x in arr[:,i]):
            arr[:,i] = le.fit_transform(arr[:,i])


    return  arr     


            
def calc_survive_female(df):

    df = df.loc[(df['Survived'] == 1) & (df['Sex'] == 'female')] 
    df = df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'])
    df = df[df['Embarked'].notna()]
    df = df[df['Age'].notna()]
    arr = df.to_numpy()
    counter = len(arr[0,:])
    le = preprocessing.LabelEncoder()
    
    for i in range(counter):
        if any(isinstance(x, str) for x in arr[:,i]):
            arr[:,i] = le.fit_transform(arr[:,i])

    return  arr      




def calc_dead_male(df):

    df = df.loc[(df['Survived'] == 0) & (df['Sex'] == 'male')] 
    df = df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'])
    df = df[df['Embarked'].notna()]
    df = df[df['Age'].notna()]
    arr = df.to_numpy()
    counter = len(arr[0,:])
    le = preprocessing.LabelEncoder()
    
    for i in range(counter):
        if any(isinstance(x, str) for x in arr[:,i]):
            arr[:,i] = le.fit_transform(arr[:,i])

    return  arr      


def calc_dead_female(df):

    df = df.loc[(df['Survived'] == 0) & (df['Sex'] == 'female')] 
    df = df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'])
    df = df[df['Embarked'].notna()]
    df = df[df['Age'].notna()]
    arr = df.to_numpy()
    counter = len(arr[0,:])
    le = preprocessing.LabelEncoder()
    
    for i in range(counter):
        if any(isinstance(x, str) for x in arr[:,i]):
            arr[:,i] = le.fit_transform(arr[:,i])

    return  arr      



def calc_average_age_class(a, b, c):
    pclass_age_list = []
    for i in range(len(a)):
        if a[i] == c:
            pclass_age = b[i]
            pclass_age_list.append(pclass_age)


    return  sum(pclass_age_list) / len(pclass_age_list)


           
  