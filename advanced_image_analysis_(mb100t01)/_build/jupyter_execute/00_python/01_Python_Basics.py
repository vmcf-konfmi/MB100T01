#!/usr/bin/env python
# coding: utf-8

# <!--NOTEBOOK_HEADER-->
# *This notebook contains material from [CBE30338](https://jckantor.github.io/CBE30338);
# content is available [on Github](https://github.com/jckantor/CBE30338.git).*
# 

# <!--NAVIGATION-->
# < [1.1 Getting Started with Python and Jupyter Notebooks](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html) | [Contents](toc.html) | [Tag Index](tag_index.html) | [1.3 Python Conditionals and Libraries](https://jckantor.github.io/CBE30338/01.03-Python-Conditionals-and-Libraries.html)<p><a href="https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/01.02-Python-Basics.ipynb"> <img align="left" src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open in Google Colaboratory"></a><p><a href="https://jckantor.github.io/CBE30338/01.02-Python-Basics.ipynb"> <img align="left" src="https://img.shields.io/badge/Github-Download-blue.svg" alt="Download" title="Download Notebook"></a>

# # Introduction to Python in Jupyter Notebook/Google Colab

# In[1]:


get_ipython().system('pip install -q -r requirements.txt')


# # 1.1 What is Google Colab
# 
# * Free to use for non-commercial use
# * Easy access to high computational power (CPUs, GPUs)
# * Easy start (no need to install or tune)
# * Connected to Google Drive
# 
# 

# # 1.2 Python Basics
# 
# **An edit of Tutorial by Jacob Gerace**

# ## 1.2.1 What I hope you'll get out of this tutorial
# * The feeling that you'll "know where to start" when you see python code.
# * (You won't be a python expert after one hour)
# * Basics to variables, lists, conditionals, functions, loops, and the numpy package.
# * Resources to look further

# ### 1.2.1.1 Why Python?
# 
# 1. Clean syntax
# 2. The same code can run on all Operating Systems
# 3. **Extensive first and third party libraries (of particular note for our purposes is NumPy)**

# ### 1.2.1.2 Markdown Sidenote
#  * This text is written in a Markdown block. Markdown is straightforward way to format writeups in Jupyter, but I won't cover it here for the sake of brevity. 
#  * See if you can use Markdown in your next homework, here's a link that explains the formatting: https://daringfireball.net/projects/markdown/syntax . 
#  * You can also look at existing Markdown examples (i.e. this worksheet) and emulate the style. Double click a Markdown box in Jupyter to show the code.
#  

# ### 1.2.1.3 LaTeX Sidenote
# * LaTeX (pronounced "La-tech") is a language itself used widely to write documents with symbolic math
# * When you add a mathematical formula to these markdown blocks, the math is in LaTeX.
# * Ex from class: $$V \frac{dC}{dt} = u(t) - Q C(t)$$ 
# * A good resource: https://en.wikibooks.org/wiki/LaTeX/Mathematics
#  
#  

# ## 1.2.2 Python Basics

# ### 1.2.2.1 Variables

# In[2]:


a='1'
print(a)


# In[3]:


#A variable stores a piece of data and gives it a name
answer = 42

#answer contained an integer because we gave it an integer!

is_it_thursday = True
is_it_wednesday = False

#these both are 'booleans' or true/false values

pi_approx = 3.1415

#This will be a floating point number, or a number containing digits after the decimal point

my_name = "Jacob"
#This is a string datatype, the name coming from a string of characters

#Data doesn't have to be a singular unit

#p.s., we can print all of these with a print command. For Example:
print(answer)
print(pi_approx)


# ### 1.2.2.2 More Complicated Data Types

# In[4]:


#What if we want to store many integers? We need a list!
prices = [10, 20, 30, 40, 50]

#This is a way to define a list in place. We can also make an empty list and add to it.
colors = []

colors.append("Green")
colors.append("Blue")
colors.append("Red")

print(colors)

#We can also add unlike data to a list
prices.append("Sixty")

#As an exercise, look up lists in python and find out how to add in the middle of a list!

print(prices)
#We can access a specific element of a list too:

print(colors[0])
print(colors[2])

#Notice here how the first element of the list is index 0, not 1! 
#Languages like MATLAB are 1 indexed, be careful!

#In addition to lists, there are tuples
#Tuples behave very similarly to lists except that you can't change them 
# after you make them

#An empty Tuple isn't very useful:
empty_tuple = ()

#Nor is a tuple with just one value:
one_tuple = ("first",)

#But tuples with many values are useful:
rosa_parks_info = ("Rosa", "Parks", 1913, "February", 4)

#You can access tuples just like lists
print(rosa_parks_info[0] + " " + rosa_parks_info[1])

# You cannot modify existing tuples, but you can make new tuples that extend 
# the information.
# I expect Tuples to come up less than lists. So we'll just leave it at that. 


# ### 1.2.2.3 Using Variables

# In[5]:


float1 = 5.75
float2 = 2.25
#Addition, subtraction, multiplication, division are as you expect

print(float1 + float2)
print(float1 - float2)
print(float1 * float2)
print(float1 / float2)

#Here's an interesting one that showed up in the first homework in 2017. Modulus: 
print(5 % 2)


# ### 1.2.2.4 Importing in Python: Math and plotting

# In[6]:


#Just about every standard math function on a calculator has a python equivalent pre made.
#however, they are from the 'math' package in python. Let's add that package!
import math as m
print(m.log(float1))
print(m.exp(float2))
print(m.pow(2,5))
# There is a quicker way to write exponents if you want:
print(2.0**5.0)

#Like in MATLAB, you can expand the math to entire lists
list3 = [1, 2, 3, 4, 5]
print(2 * list3)


# In[7]:


#We can plot easily in Python like in matlab, just import the relevant package!
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

x_vals = [-2, -1, 0, 1, 2]
y_vals = [-4, -2, 0, 2, 4]
plt.plot(x_vals, y_vals)


# ### 1.2.2.5 Loops in Python

# In[8]:


#Repeat code until a conditional statement ends the loop

#Let's try printing a list
fib = [1, 1, 2, 3, 5, 8]

#While loops are the basic type
i = 0
while(i < len(fib)):
    print(fib[i])
    i = i + 1
    
#In matlab, to do the same thing you would have the conditional as: counter < (length(fib) + 1)
#This is because matlab starts indexing at 1, and python starts at 0.
    
#The above type of loop is so common that the 'for' loop is the way to write it faster.

print("Let's try that again")
#This is most similar to for loops in matlab
for i in range(0, len(fib)) :
    print(fib[i])

print("One more time:")
#Or you can do so even neater
for e in fib:
    print(e)


# ## 1.2.3 Additional Resources
# * If you still feel VERY lost: [Code Academy](https://www.codecademy.com/learn/python)
# 
# * If you want a good reference site: [Official Python Reference](https://docs.python.org/2/reference/)
# 
# * If you want to learn python robustly: [Learn Python the Hard Way](https://learnpythonthehardway.org/book/)
# 
# * Feel free to contact me at: **jgerace (at) nd (dot) edu**
# 

# <!--NAVIGATION-->
# < [1.1 Getting Started with Python and Jupyter Notebooks](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html) | [Contents](toc.html) | [Tag Index](tag_index.html) | [1.3 Python Conditionals and Libraries](https://jckantor.github.io/CBE30338/01.03-Python-Conditionals-and-Libraries.html)<p><a href="https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/01.02-Python-Basics.ipynb"> <img align="left" src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open in Google Colaboratory"></a><p><a href="https://jckantor.github.io/CBE30338/01.02-Python-Basics.ipynb"> <img align="left" src="https://img.shields.io/badge/Github-Download-blue.svg" alt="Download" title="Download Notebook"></a>
