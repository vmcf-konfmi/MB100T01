#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# Inspiration and some of the parts came from: Python Data Science [GitHub repository](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master), [MIT License](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-CODE) and [Introduction to Pandas](https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb) by Google, [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
# 
# If running this from Google Colab, uncomment the cell below and run it. Otherwise, just skip it.

# In[1]:


#!pip install seaborn
#!pip install watermark


# In[9]:


import pandas as pd
import seaborn as sns
from scipy import stats


# ## Learning Objectives:
# 
#  * descriptive statistics/EDA
#  * corr matrix
# 
# For this notebook, we will use the california housing dataframes.

# In[5]:


california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe


# ## Exploring Data

# As shown above, after loading a large `DataFrame`, it may be a bit hard to have a good overview of what is inside it just by looking at a few rows. Thus, the `DataFrame.describe` method is useful to show interesting statistics about a `DataFrame`.

# In[6]:


california_housing_dataframe.describe()


# Another useful function is `DataFrame.head`, which displays the first few records of a `DataFrame`. You can give it a number of rows to display.

# In[7]:


california_housing_dataframe.head(10)


# Or `DataFrame.tail`, which displays the last few records of a `DataFrame`:

# In[8]:


california_housing_dataframe.tail()


# ## Correletaion Matrix
# 
# Consider the table of measurements below.

# In[23]:


blobs_statistics = pd.read_csv('../../data/blobs_statistics.csv', index_col=0)
blobs_statistics.head()


# After measuring many features / properties, it is often common that some of them are strongly correlated and may not bring much new information. In pandas, we can calculate correlation among columns like this.

# In[24]:


blobs_statistics.corr()


# It can be hard to read in numeric format. I wonder if there is beter way how to look at the data?
# 
# Below we take a quick shortcut to seaborn to show how the correlation can be displayed as a heatmap.

# In[25]:


# calculate the correlation matrix on the numeric columns
corr = blobs_statistics.select_dtypes('number').corr()

# plot the heatmap
sns.heatmap(corr, cmap="Blues", annot=False)


# **Watermark**

# In[15]:


from watermark import watermark
watermark(iversions=True, globals_=globals())
print(watermark())
print(watermark(packages="watermark,numpy,pandas,seaborn,pivottablejs"))

