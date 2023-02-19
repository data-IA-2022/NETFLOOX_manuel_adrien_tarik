# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:38:38 2023

@author: Utilisateur
"""

import pandas as pd
import numpy as np
from df_loading import datasets as dts
import scipy.stats as ss

df=dts['tables']['films'][:1000].dropna()

print()
print()
print(df.shape)
print()
print()

for name_group in df.groupby('genres'):

    try:
        samples = [condition[1] for condition in name_group[1].groupby('startYear')['averageRating']]
    
   
        f_val, p_val = ss.f_oneway(*samples)
        print('------------------------')
        print('Name: {}, F value: {:.3f}, p value: {:.3f}'.format(name_group[0], f_val, p_val))
        print('------------------------')
    except:
        pass

    



