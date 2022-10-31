#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize']= (12,6)
sns.set_style('whitegrid')


# In[5]:


#read csv file

motor = pd.read_csv('sales_data.csv', parse_dates=['date'])
motor.head(5)


# In[6]:


#understand data

motor.shape


# In[7]:


motor.info


# In[10]:


motor.isnull().sum()


# ##### Observations
# 
# - There are no null values in the dataset
# - There is no duplicate dataset

# In[12]:


dulpicate = motor[motor.duplicated()]
dulpicate


# ## Data Visualization 

# In[13]:


motor.warehouse.unique()


# In[14]:


motor.client_type.unique()


# In[15]:


motor.product_line.unique()


# In[16]:


motor.payment.unique()


# In[17]:


motor.warehouse.unique()


# ## Observations
# 
# There are 3 warehouse , 2 client types, 6 product line payment methods.

# Total sales for each payment method

# In[33]:


total_sales_payment = motor.groupby('payment').total.agg([sum]).reset_index()
total_sales_payment


# In[40]:


pm= sns.barplot(x='payment',y='sum',data=total_sales_payment)
plt.title('Total sales per payment', fontweight='bold',fontsize=16)
plt.xlabel('payment', fontweight='bold',fontsize=16)
plt.ylabel('total sales',fontweight='bold',fontsize=16);
for i in am.containers:
    pm.bar_label(i)


# ## Observations
# 
# We can see here that most payment were made through tranfer as compared to cash and credit card.

# ### Average Unit Price for each prduct line

# In[37]:


av_unit_price = motor.groupby('product_line').unit_price.mean().reset_index()
av_unit_price


# In[39]:


am= sns.barplot(x='product_line',y='unit_price',data=av_unit_price)
plt.title('Average unit price', fontweight='bold',fontsize=16)
plt.xlabel('product_line', fontweight='bold',fontsize=16)
plt.ylabel('unit_price',fontweight='bold',fontsize=16);
for i in am.containers:
    am.bar_label(i)


# In[42]:


av_purchase_price = motor.groupby('client_type').total.mean().reset_index()
av_purchase_price


# In[43]:


my_colors = ['red','teal']
plt.barh(av_purchase_price.client_type,av_purchase_price.total, color=my_colors)
plt.title('Avg price/client',fontsize=14)
plt.xlabel('client', fontsize=14)
plt.ylabel('total',fontsize=14)
plt.grid(False)
plt.yticks(rotation=90)
plt.show


# ### Total purchase value by product line

# In[46]:


t_purchase_price = motor.groupby('product_line').total.agg([sum]).reset_index()
t_purchase_price


# In[47]:


product_line = ['Breaking system', 'Electrical system','Engine','Frame & Body','Miscellaneous', 'suspension and traction']
sales = np.array([38350.15,43612.71,37945.38,69024.73,27165.82,73014.21])
my_explode = [0,0,0,0,0,0.1]
plt.pie(sales, labels=product_line, explode=my_explode,autopct='%1.1f%%')
plt.title('total purchase price');


# In[ ]:




