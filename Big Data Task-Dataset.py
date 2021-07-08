#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import random
import numpy as np
from random import randrange
import names


classes=['pilates',' group fitness','kickboxing','climbing','dance', 'powerlifting','running']

#Age group 50-70 15k people
print(df)




df = pd.DataFrame(columns=['Member_ID','Name','Age','Gender','Discipline','Time of Entry','Facility_ID'])





#For Ages 50-70
for i in range(1,10000):
    a='M_'+str(i)
    df.at[i,'Member_ID']=a
    df.at[i,'Name']=names.get_full_name()
    b=[randrange(50,70)]
    df.at[i,'Age']=b
    dc=np.random.choice(7,1, p=[0.5, 0.2,0.025,0.025,0.05,0.01,0.19])
    c=classes[int(dc)]
    gchoice=['Male','Female']
    df.at[i,'Gender']=random.choice(gchoice)
    #discipline chosen with probabilities denoted in dc
    df.at[i,'Discipline']=c
    time=["09:00-10:00"]*4+["10:00-11:00"]*3+["11:00-12:00"]*2+["12:00-13:00"]*2+["13:00-14:00"]*2+["14:00-15:00"]*3+["15:00-16:00"]*2+["16:00-17:00"]*1+["17:00-18:00"]*1+["18:00-19:00"]*1+["19:00-20:00"]*1
    #Each time picked with probability kn/sum(ki)
    d=random.choice(time)
    df.at[i,'Time of Entry']=d
    e='Facility_'+str(randrange(101))
    df.at[i,'Facility_ID']=e


#The rest of the data generation algorithm follows the same logic


#For Ages 35-50
for i in range(10000,30000):
    a='M_'+str(i)
    df.at[i,'Member_ID']=a
    df.at[i,'Name']=names.get_full_name()
    b=[randrange(35,50)]
    df.at[i,'Age']=b
    dc=np.random.choice(7,1, p=[0.2, 0.2,0.15,0.15,0.05,0.05,0.2])
    c=classes[int(dc)]
    gchoice=['Male','Female']
    df.at[i,'Gender']=random.choice(gchoice)
    df.at[i,'Discipline']=c
    time=["09:00-10:00"]*3+["10:00-11:00"]*1+["11:00-12:00"]*1+["12:00-13:00"]*3+["13:00-14:00"]*2+["14:00-15:00"]*1+["15:00-16:00"]*1+["16:00-17:00"]*1+["17:00-18:00"]*1+["18:00-19:00"]*1+["19:00-20:00"]*1
    d=random.choice(time)
    df.at[i,'Time of Entry']=d
    e='Facility_'+str(randrange(101))
    df.at[i,'Facility_ID']=e





#For Ages 18-35
for i in range(30000,70001):
    a='M_'+str(i)
    df.at[i,'Member_ID']=a
    df.at[i,'Name']=names.get_full_name()
    b=[randrange(18,35)]
    df.at[i,'Age']=b
    dc=np.random.choice(7,1, p=[0.15, 0.15,0.15,0.15,0.15,0.10,0.15])
    c=classes[int(dc)]
    gchoice=['Male','Female']
    df.at[i,'Gender']=random.choice(gchoice)
    df.at[i,'Discipline']=c
    time=["09:00-10:00"]*2+["10:00-11:00"]*2+["11:00-12:00"]*1+["12:00-13:00"]*3+["13:00-14:00"]*2+["14:00-15:00"]*2+["15:00-16:00"]*2+["16:00-17:00"]*2+["17:00-18:00"]*4+["18:00-19:00"]*4+["19:00-20:00"]*4
    d=random.choice(time)
    df.at[i,'Time of Entry']=d
    e='Facility_'+str(randrange(101))
    df.at[i,'Facility_ID']=e




np.random.shuffle(df['Member_ID'])




df.to_csv('big_data_task.csv', encoding='utf-8')

