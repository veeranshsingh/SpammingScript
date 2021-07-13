# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 01:51:37 2021

@author: veeransh
"""

import pywhatkit as pwk
import pandas as pd
import datetime
from time import sleep

df = pd.read_csv('sample1 - sample1.csv')

for index, row in df.iterrows():
    sleep(12)
    hourRN = datetime.datetime.now().time().hour
    minutesRN = datetime.datetime.now().time().minute + 5
    if minutesRN >= 60:
        if hourRN < 23:
            hourRN += 1
        else:
            
            hourRN = 0
        minutesRN -= 60
    try:
        pwk.sendwhatmsg_instantly("+91"+str(row['Phone Number']), 
                              "Hi "+row['Name']+" this is veeransh singh ", 
                              hourRN, minutesRN)
    except:
        print("Could Not send msg to:",row['Name'],":",row['Phone Number'])