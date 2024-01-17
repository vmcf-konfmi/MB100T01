#!/usr/bin/env python
# coding: utf-8

# # Basic Operations

# Inspiration and some of the parts came from: Python Data Science [GitHub repository](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master), [MIT License](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-CODE) and [Introduction to Pandas](https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb) by Google, [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
# 
# If running this from Google Colab, uncomment the cell below and run it. Otherwise, just skip it.

# In[1]:


#!pip install seaborn
#!pip install watermark


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns


# ## Learning Objectives:
# 
#  * operations
#   * selection
#   * filtering
#   * concat
#   * NaNs
# 

# For this notebook, we will continue using the cities and california housing dataframes.

# In[3]:


city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities_dataframe = pd.DataFrame({ 'City name': city_names, 'Population': population })
cities_dataframe


# In[4]:


california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe.head()


# ## Manipulating Data
# 
# ### Applying functions
# 
# You may apply Python's basic arithmetic operations to `Series`. For example:

# In[5]:


population / 1000


# *pandas* `Series` can be used as arguments to most NumPy functions:

# In[6]:


np.log(population)


# For more complex single-column transformations, you can use `Series.apply`. Like the Python [map function](https://docs.python.org/2/library/functions.html#map),
# `Series.apply` accepts as an argument a [lambda function](https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions), which is applied to each value.
# 
# The example below creates a new `Series` that indicates whether `population` is over one million:

# In[7]:


big_city = population.apply(lambda val: val > 1000000)
big_city


# ### Filtering

# One can use this result as a binary mask to make a sub-dataframe.

# In[8]:


cities_dataframe[big_city]


# Here is another way of generating a binary mask without explicitly using a `lamba` function.

# In[9]:


big_city = cities_dataframe['Population'] > 1000000
big_city


# ### Adding new columns
# 
# Modifying `DataFrames` is also straightforward. For example, the following code adds two `Series` to an existing `DataFrame`. One of them is the result of a computation of 2 existing columns.

# In[10]:


cities_dataframe['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities_dataframe['Population density'] = cities_dataframe['Population'] / cities_dataframe['Area square miles']
cities_dataframe


# ### Concatenating DataFrames
# 
# Let's imagine we collect another similar data sample, like the one below.

# In[11]:


city_names = pd.Series(['Sao Paulo', 'Sao Luis', 'Salvador'])
population = pd.Series([12400232, 1108975, 2886698])

another_cities_dataframe = pd.DataFrame({ 'City name': city_names, 'Population': population })

another_cities_dataframe['Area square miles'] = pd.Series([587.34, 319.36, 268])
another_cities_dataframe['Population density'] = another_cities_dataframe['Population'] / another_cities_dataframe['Area square miles']
another_cities_dataframe


# Before concatenating, it is probably a good idea to insert an identifier column so that we keep track where data came from.
# 
# We can easily do that by creating a new column in each dataframe **before** concatenating.

# In[12]:


cities_dataframe['Country'] = 'USA'
another_cities_dataframe['Country'] = 'Brazil'


# We can now concatenate similar dataframes with the `pandas.concat` functions.

# In[13]:


result = pd.concat([cities_dataframe, another_cities_dataframe])
result


# We now have a longer dataframe with some repeated indices. To have unique indices, we can use `.reset_index`.

# In[14]:


result = result.reset_index(drop=True)
result


# ### NaNs
# 
# `DataFrame` objects can be created by passing a `dict` mapping `string` column names to their respective `Series`. If the `Series` don't match in length, missing values are filled with special [NA/NaN](http://pandas.pydata.org/pandas-docs/stable/missing_data.html) values. We cannot assume what these values are, because that would distort th results. So we need to deal with these NaNs values.

# We can test the missing values using `isnull()` function.

# We can work with one of the `seaborn` training datasets *Penguins*

# In[15]:


penguins = sns.load_dataset("penguins")


# In[16]:


penguins.isnull()


# But it is more practical to test if there are any NaNs, than looking for it. We can use `.isnull().values.any()` approach.

# In[17]:


penguins.isnull().values.any()


# Or we can explore each column using `.isnull().sum()`.

# In[18]:


penguins.isnull().sum()


# We will want to drop all rows with unknown entries with `.dropna()` function.

# In[19]:


penguins_cleaned = penguins.dropna()
penguins_cleaned.isnull().sum()


# ## Exercise
# 
# The table below contains shape and intensity measurements from a biological sample. Make a subset with the columns `Area` and `Mean`. Remove all rows that contain NaNs from it and count the remaining rows.
# 
# Afterwards, take the initial table again and make a new subset with the columns `Major` and `Minor`. Remove NaNs and count the remaining rows again.
# 
# What do you conclude?

# In[21]:


dataframe = pd.read_csv('../../data/Results.csv', index_col=0, delimiter=';')
dataframe


# In[ ]:





# **Watermark**

# In[16]:


from watermark import watermark
watermark(iversions=True, globals_=globals())
print(watermark())
print(watermark(packages="watermark,numpy,pandas,seaborn,pivottablejs"))

