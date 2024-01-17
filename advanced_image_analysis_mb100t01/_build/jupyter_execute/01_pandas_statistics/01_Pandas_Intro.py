#!/usr/bin/env python
# coding: utf-8

# # Introduction to Pandas
# 
# [*pandas*](http://pandas.pydata.org/) is a column-oriented data analysis API. It's a great tool for handling and analyzing input data, and many ML frameworks support *pandas* data structures as inputs.
# Although a comprehensive introduction to the *pandas* API would span many pages, the core concepts are fairly straightforward, and we'll present them below. For a more complete reference, the [*pandas* docs site](http://pandas.pydata.org/pandas-docs/stable/index.html) contains extensive documentation and many tutorials.

# Inspiration and some of the parts came from: Python Data Science [GitHub repository](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master), [MIT License](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/LICENSE-CODE) and [Introduction to Pandas](https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb) by Google, [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
# 
# If running this from Google Colab, uncomment the cell below and run it. Otherwise, just skip it.

# In[1]:


#!pip install watermark


# ## Learning Objectives:
# 
#  * Gain an introduction to the *DataFrame* and *Series* data structures of the pandas library
# 
#  * Import CSV data into a pandas *DataFrame*
# 
#  * Access and manipulate data within a *DataFrame* and *Series*
# 
#  * Export *DataFrame* to CSV

# ## Basic Concepts
# 
# The following line imports the *pandas* API and prints the API version:

# In[2]:


import pandas as pd
pd.__version__


# The primary data structures in *pandas* are implemented as two classes:
# 
#   * **`DataFrame`**, which you can imagine as a relational data table, with rows and named columns.
#   * **`Series`**, which is a single column. A `DataFrame` contains one or more `Series` and a name for each `Series`.
# 
# The data frame is a commonly used abstraction for data manipulation. Similar implementations exist in [Spark](https://spark.apache.org/) and [R](https://www.r-project.org/about.html).

# ### pandas.Series
# 
# One way to create a `Series` is to construct a `Series` object. For example:

# In[3]:


pd.Series(['San Francisco', 'San Jose', 'Sacramento'])


# ### pandas.DataFrame

# `DataFrame` objects can be created by passing a `dict` mapping `string` column names to their respective `Series`. If the `Series` don't match in length, missing values are filled with special [NA/NaN](http://pandas.pydata.org/pandas-docs/stable/missing_data.html) values. Example:

# In[4]:


city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

cities_dataframe = pd.DataFrame({ 'City name': city_names, 'Population': population })
cities_dataframe


# #### Reading a DataFrame from a file

# But most of the time, you load an entire file into a `DataFrame`. The following example loads a file with California housing data. Run the following cell to load the data and create feature definitions:

# In[5]:


california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe.head()
#california_housing_dataframe.tail()


# If you need to take a peak to documentation, there is always fast way to use **?** after function.

# In[6]:


get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# ### Selecting Columns, Rows and Creating Subsets
# 
# We index DataFrames by columns, like this:

# In[7]:


california_housing_dataframe['population']


# We can get more columns by passing their names as a list. Furthermore, we can store this "sub-dataframe" in a new variable.

# In[8]:


sub_dataframe = california_housing_dataframe[ ['population', 'households'] ]
sub_dataframe


# If we want to get a single row, the proper way of doing that is to use the `.loc` method:

# In[9]:


row_with_index_2 = california_housing_dataframe.loc[2,  ['population', 'households'] ]
row_with_index_2


# In addition, *pandas* provides an extremely rich API for advanced [indexing and selection](http://pandas.pydata.org/pandas-docs/stable/indexing.html) that is too extensive to be covered here.

# ## Saving data
# 
# A `DataFrame` can be saved as a `.csv` file with the `.to_csv` method.

# In[16]:


cities_dataframe.to_csv('cities_out.csv', index=False, sep=";")


# ## Exercise
# 
# From the following loaded CSV file, create a table that only contains these columns:
# 
# - minor_axis_length
# - major_axis_length
# - aspect_ratio

# In[16]:


blobs_df = pd.read_csv('../../data/blobs_statistics.csv')
blobs_df


# In[ ]:





# **Watermark**

# In[19]:


from watermark import watermark
watermark(iversions=True, globals_=globals())
print(watermark())
print(watermark(packages="watermark,numpy,pandas,seaborn,pivottablejs"))

