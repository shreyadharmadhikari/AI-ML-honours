#!/usr/bin/env python
# coding: utf-8

# <h2>Assignment No : 1</h2>

# In[10]:


# Name : Shreya Dharmadhikari
# Roll No : 31014
# Batch : T1 Batch Computer
# Title : Calculate Mean, Variance, Standard Deviation, Covariance, Correlation and Standard Error.
# Problem Statement : Compute Estimators of the main statistical measures like Mean, Variance, Standard
#                     Deviation, Covariance, Correlation and Standard error with respect to any example.
#                     Display graphically the distribution of samples.


# In[11]:


import pandas as pd

import numpy as np
import matplotlib.pyplot as plt                    #import required libraries in python
import seaborn as sns                                  


# In[12]:


df=pd.read_csv(r"C:\Users\Suhas\Desktop\AI and ML\Iris_dataset.csv")   #Read CSV file


# In[13]:


sepal_length=df['sepal length']
sepal_width=df['sepal width']
petal_length=df['petal length']
petal_width=df['petal width']
df_class=df['class']


# <h3> Mean </h3>

# In[14]:


mean_sepal_length=np.mean(sepal_length)               #calculating mean and storing it in defined variable
print('Mean of sepal lengths :',mean_sepal_length)    #numpy.mean() function is used to compute the arithmetic mean along the specified axis.


# In[15]:


mean_sepal_width=np.mean(sepal_width)                 #calculating mean and storing it in defined variable
print('Mean of sepal widths :',mean_sepal_width)


# In[16]:


mean_petal_length=np.mean(petal_length)               #calculating mean and storing it in defined variable
print('Mean of petal lengths :',mean_petal_length)


# In[17]:


mean_petal_width=np.mean(petal_width)                 #calculating mean and storing it in defined variable
print('Mean of petal widths :',mean_petal_width)


# In[18]:


plt.scatter(sepal_width,sepal_length)          #predefined function for scatter plot
plt.title('Mean sepal width')                  #title of the graph
plt.xlabel('sepal width(in cms)')              #label for x-axis
plt.ylabel('sepal length(in cms)')             #label for y-axis
plt.axvline(x=mean_sepal_width,color='red',linewidth=4,linestyle='--')     #plot vertical line parallel to Y-axis with given value of X


# In[19]:


plt.scatter(sepal_width,sepal_length)                   #predefined function for scatter plot
plt.title('Mean sepal length')
plt.xlabel('sepal width(in cms)')
plt.ylabel('sepal length(in cms)')
plt.axhline(y=mean_sepal_length,color='red',linewidth=4,linestyle='--')


# In[20]:


plt.scatter(petal_width,petal_length)                   #predefined function for scatter plot
plt.title('Mean petal width')
plt.xlabel('petal width(in cms)')
plt.ylabel('petal length(in cms)')
plt.axvline(x=mean_petal_width,color='yellow',linewidth=4,linestyle='--')


# In[21]:


plt.scatter(petal_width,petal_length)               #predefined function for scatter plot
plt.title('Mean petal length')
plt.xlabel('petal width(in cms)')
plt.ylabel('petal length(in cms)')
plt.axhline(y=mean_petal_length,color='yellow',linewidth=4,linestyle='--')


# <h3> Variance </h3>

# In[22]:


var_sw=np.var(sepal_width)                           #calculating variance and storing it in defined variable
print('Variance of sepal width :',var_sw)            #We can find variance of specfic column using numpy.var() method
var_sl=np.var(sepal_length)                          #calculating variance and storing it in defined variable
print('Variance of sepal length :',var_sl)


# In[23]:


plt.scatter(sepal_width,sepal_length)               #predefined function for scatter plot
plt.title('Variance of sepal width')
plt.xlabel('sepal width(in cms)')
plt.ylabel('sepal length(in cms)')
plt.axvline(x=var_sw,color='green',linewidth=3)


# In[24]:


plt.scatter(sepal_width,sepal_length)                 #predefined function for scatter plot
plt.title('Variance of sepal length')
plt.xlabel('sepal width(in cms)')
plt.ylabel('sepal length(in cms)')
plt.axhline(y=var_sl,color='green',linewidth=3)


# <h3> Standard deviation </h3>

# In[25]:


sd_sw=np.std(sepal_width)                              #calculating standard deviation and storing it in defined variable
print('Standard deviation of sepal width:',sd_sw)      #Standard deviation can be calculated using numpy.std() function
sd_pw=np.std(petal_width)                              #calculating standard deviation and storing it in defined variable
print('Standard deviation of petal width:',sd_pw)


# In[26]:


plt.title('Standard deviation of sepal width')
plt.scatter(sepal_width,sepal_length)
plt.xlabel('sepal width(in cms)')
plt.ylabel('sepal length(in cms)')
plt.axvline(x=sd_sw,color='violet',linewidth=4,linestyle='-')


# In[27]:


plt.title('Standard deviation of petal width')
plt.scatter(petal_width,petal_length)                       #predefined function for scatter plot               
plt.xlabel('petal width(in cms)')
plt.ylabel('petal length(in cms)')
plt.axvline(x=sd_pw,color='violet',linewidth=4,linestyle='-')


# <h3> Covariance </h3>

# In[28]:


cov_sepal=np.cov(sepal_width,sepal_length)                  #calculating covariance and storing it in defined variable
print('covariance matrix between sepal width and sepal length is :',cov_sepal)


# In[29]:


cov_sw=sepal_width.cov(sepal_length)                        #calculating covariance and storing it in defined variable
print('Covariance between sepal width and sepal length is :',cov_sw)


# In[30]:


np.cov(sepal_width)


# In[31]:


np.cov(sepal_length)


# <h3> Correlation </h3>

# In[32]:


cor_s=sepal_width.corr(sepal_length)                       #calculating correlation and storing it in defined variable
print('Correlation coefficient between sepal width and sepal length :',cor_s)


# In[33]:


cor_p=petal_width.corr(petal_length)                       #calculating correlation and storing it in defined variable
print('Correlation coefficient between petal width and petal length :',cor_p)


# <h3> Standard error </h3>

# In[34]:


from scipy.stats import sem
ss=sem(sepal_width)                                       #calculating standard error and storing it in defined variable
print('Standard error of standard mean of sepal width :',ss)


# In[35]:


from scipy.stats import sem
sl=sem(petal_length)
print('Standard error of standard mean of petal length :',sl)


# <h3>Graphical distribution of sample</h3>

# In[36]:


sns.FacetGrid(df, hue="class",size=5).map(plt.scatter,"sepal width","sepal length").add_legend();


# In[37]:


sns.FacetGrid(df, hue="class",size=5).map(plt.scatter,"petal width","petal length").add_legend();

