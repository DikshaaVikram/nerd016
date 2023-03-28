#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt


# In[12]:


df1 = pd.read_excel('C:/Users/Dikshaa Vikram/Desktop/NPTEL Data Analytics/TRUCKING.xlsx')
df1


# In[14]:


import matplotlib.pyplot as plt
plt.scatter(df1['x1'],df1['travel_time'], color = "green")
plt.ylabel('Travel time')
plt.title(' Simple liner regression with Miles travelled ')


# In[20]:


import matplotlib.pyplot as plt
plt.scatter(df1['n_of_deliveries'],df1['travel_time'], color = "red")
plt.scatter(df1['x1'],df1['travel_time'], color = "green")
plt.ylabel('Travel time')
plt.title(' Multiple regression model ')


# In[21]:


import matplotlib.pyplot as plt
plt.scatter(df1['n_of_deliveries'],df1['travel_time'], color = "red")
plt.ylabel('Travel time')
plt.title(' Simple liner regression with no of deliveries ')


# In[26]:


Reg1 = ols(formula = "travel_time ~ x1", data = df1)
Fit1 = Reg1.fit()
print(Fit1.summary())


# In[27]:


Reg2 = ols(formula = "travel_time ~ x1 + n_of_deliveries", data = df1)
Fit2 = Reg2.fit()
print(Fit2.summary())


# In[ ]:




