# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


sk = pd.read_csv('NFLX Historical Data.csv',usecols=(0,1,2,3,4))


PL_avg = sk[['Price','Open','High','Low']].mean(axis=1)




obs = np.arange(1,len(sk)+1,1)


plt.plot(obs,PL_avg,'r',label = 'MY FIRST PLOT')


