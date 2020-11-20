# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 01:25:53 2020

@author: 
"""

#IMPORTING THE LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt




#READING THE DATA FROM FILES
data = pd.read_csv("advertising.csv")
data.head()




#TO VISUALISE DATA
fig , axs = plt.subplots(1,3,sharey=(True))
data.plot(kind = 'scatter',x ='TV',y='Sales',ax=axs[0],figsize=(16,8))
data.plot(kind = 'scatter',x ='Radio',y='Sales',ax=axs[1])
data.plot(kind = 'scatter',x ='Newspaper',y='Sales',ax=axs[2])




#CREATING X&Y FOR LINEAR REGRESSION
feature_cols = ['TV']
X = data[feature_cols]
y = data.Sales






#REPORTING LINEAR REGRESSION ALGO FOR SIMPLE LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)




Y = a+bx

#CR
result = 6.9748214882298925+0.05546477*78
print(result)


#CREATING A DATAFRAME WITH MIN & MAX VALU OF THE TABLE
X_new = pd.DataFrame ({'TV':[data.TV.min(), data.TV.max()]})
X_new.head()


preds = lr.predict(X_new)
preds


data.plot(kind = 'scatter',x='TV',y= 'Sales')

plt.plot(X_new,preds,c='black',linewidth=2)



data.plot(kind = 'scatter',x='Radio',y= 'Sales')

plt.plot(X_new,preds,c='Red',linewidth=4)



data.plot(kind = 'scatter',x='Newspaper',y= 'Sales')

plt.plot(X_new,preds,c='Green',linewidth=1)



import statsmodels.formula.api as smf
lr = smf.ols(formula = 'Sales ~ TV', data=data).fit()
lr.conf_int()



#FINDING THE PROBABILITY VALUES
lr.pvalues

#FINDING THE R-SQUARED VALUES
lr.rsquared


#MUTILINEAR REGRESSION
feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
y = data.Sales


lr = LinearRegression()
lr.fit(X,y)


print(lr.intercept_)
print(lr.coef_)


lr = smf.ols(formula = 'Sales ~ TV+Radio+Newspaper',data=data).fit()
lr.conf_int()
lr.summary()



lr = smf.ols(formula = 'Sales ~ TV+Radio',data=data).fit()
lr.conf_int()
lr.summary()



lr = smf.ols(formula = 'Sales ~ TV+Newspaper',data=data).fit()
lr.conf_int()
lr.summary()



lr = smf.ols(formula = 'Sales ~ Radio+Newspaper',data=data).fit()
lr.conf_int()
lr.summary()



