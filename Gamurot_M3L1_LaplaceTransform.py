#!/usr/bin/env python
# coding: utf-8

# # **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;"><center>Module 3</center></span>**
# 
# # **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;"><center>Lesson 1: Introduction to Laplace Transform</center></span>**

# ## **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;">Objective:</span>**
#  - to create a program that can perform and solve specific laplace transform problems
#     

# ## **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;">Sympy Modules and Printing Function</span>**

# In[1]:


import sympy as sp
from sympy import oo
from sympy.interactive import printing
printing.init_printing(use_latex=True) 


# ## **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;">1.1 Laplace Transforms of Elementary Functions</span>**

# **Problem 1.** Using a standard list of Laplace transforms, determine the following:
# 
#  (a) $\mathcal{L}\{1 + 2t - \frac{1}{3}t^4\}$
# 
#  (b) $\mathcal{L}\{5e^{2t} - 3e^{-t}\}$ 
# 
# 

# **Solution/Code**

# In[2]:


t, s, a, b = sp.symbols('t s a b')
print('Output:\n')
# a
eq1 = 1 + 2*t - (1/3)*(t**4)
display(a)
display(sp.laplace_transform(eq1,t,s)[0])

# b
eq2 = 5*(sp.exp(2*t)) - 3*(sp.exp(-t))
display(b)
display(sp.laplace_transform(eq2,t,s)[0])


# **Problem 2.** Find the Laplace transform of:
# 
# (a) $6sin3t - 4cos5t$
# 
# (b) $2cosh2\theta - sinh3\theta$

# **Solution/Code**

# In[3]:


t, s, a, b, theta = sp.symbols('t s a b theta')
print('Output:\n')

# a
eq1 = 6*sp.sin(3*t) - 4*sp.cos(5*t)
display(a)
display(sp.laplace_transform(eq1,t,s)[0])

# b
eq2 = 2*sp.cosh(2*theta) - sp.sinh(3*theta)
display(b)
display(sp.laplace_transform(eq2,theta,s)[0])


# **Problem 3.** Prove that
# 
# (a) $\mathcal{L}\{sin~at\} = \frac{a}{s^2 + a^2} ~~~~ $ (b) $\mathcal{L}\{t^2\} = \frac{2}{s^3}$
# 
# (c) $\mathcal{L}\{cosh~at\} = \frac{s}{s^2 - a^2}$

# **Solution/Code**

# In[4]:


t, s, a, b, c = sp.symbols('t s a b c')
print('Output:\n')

# a
eq1 = sp.sin(a*t)
display(a)
display(sp.laplace_transform(eq1,t,s)[0])

# b
eq2 = t**2
display(b)
display(sp.laplace_transform(eq2,t,s)[0])

# c
eq3 = sp.cosh(a*t)
display(c)
display(sp.laplace_transform(eq3,t,s)[0])


# **Problem 4.** Determine the Laplace transforms of:
# 
# (a) $sin^2t ~~~$ (b) $cosh^23x$

# **Solution/Code**

# In[5]:


t, s, a, b, x = sp.symbols('t s a b x')
print('Output:\n')

# a
eq1 = (sp.sin(t))**2
display(a)
display(sp.laplace_transform(eq1,t,s)[0])

# b
eq2 = (sp.cosh(3*x))**2
display(b)
display(sp.laplace_transform(eq2,x,s)[0])


# **Problem 5.** Find the Laplace transform of $3sin(\omega t + \alpha)$, where $\omega$ and $\alpha$ are constants.

# **Solution/Code**

# In[6]:


t, s, a, b, x = sp.symbols('t s a b x')
theta, omega, alpha = sp.symbols('theta omega alpha', real = True, constant = True)
print('Output:\n')

# a
eq1 = 3*(sp.sin(omega*t + alpha))
display(sp.laplace_transform(eq1,t,s)[0])


# ## **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;">1.2 The Laplace Transform of $e^{at}~f(t)$</span>**

# **Problem 6.** Determine $(a)~\mathcal{L}\{2t^4e^{3t}\}~~ (b)~\mathcal{L}\{4e^{3t}cos5t\}$.

# **Solution/Code**

# In[7]:


t, s, a, b = sp.symbols('t s a b')
print('Output:\n')

# a
eq1 = 2*(t**4)*sp.exp(3*t)
display(a)
display(sp.laplace_transform(eq1,t,s)[0])

# b
eq2 = 4*((sp.exp(3*t))*(sp.cos(5*t)))
display(b)
display(sp.laplace_transform(eq2,t,s)[0])


# **Problem 7.** Determine $(a)~\mathcal{L}\{e^{-2t}sin3t\}~~ (b)~\mathcal{L}\{3e^{\theta}cosh4\theta\}$.

# **Solution/Code**

# In[8]:


t, s, a, b = sp.symbols('t s a b')
print('Output:\n')

# a
eq1 = ((sp.exp(-2*t))*(sp.sin(3*t)))
display(a)
display(sp.laplace_transform(eq1,t,s)[0])

# b
eq2 = 3*((sp.exp(theta))*(sp.cosh(4*theta)))
display(b)
display(sp.laplace_transform(eq2,theta,s)[0])


# **Problem 8.** Determine the Laplace transforms of $(a)~5e^{-3t}sinh2t ~~ (b)~2e^{3t}(4cos2t - 5sin2t)$

# **Solution/Code**

# In[9]:


t, s, a, b = sp.symbols('t s a b')
print('Output:\n')

# a
eq1 = 5*((sp.exp(-3*t))*(sp.sinh(2*t)))
display(a)
display(sp.laplace_transform(eq1,t,s)[0])

# b
eq2 = 2*sp.exp(3*t)*(4*sp.cos(2*t) - 5*sp.sin(2*t))
display(b)
display(sp.laplace_transform(eq2,t,s)[0])


# **Problem 9.** Show that
# 
# $\mathcal{L}\{3e^{-\frac{1}{2}x}sin^2x\} = \frac{48}{(2s+1)(4s^2+4s+17)}$

# **Solution/Code**

# In[10]:


x, s,  = sp.symbols('x s')
print('Output:\n')

eq1 = (3/2)*((sp.exp((-1/2)*x)))
eq2 = (3/2)*((sp.exp((-1/2)*x)*sp.cos(2*x)))
eq3 = sp.laplace_transform(eq1-eq2,x,s)
eq3_numerator = (sp.fraction(eq3[0])[0])*4
eq3_denominator = (sp.fraction(eq3[0])[1])*4
display(eq3_numerator/eq3_denominator)


# ## **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;">1.3 The Laplace Transforms of Derivatives</span>**

# **Problem 10.** Use the Laplace transform of the first derivative to derive:
# 
# $(a)~\mathcal{L}\{k\} = \frac{k}{s} ~~~~ (b)~\mathcal{L}\{2t\} = \frac{2}{s^2}$ 
# 
# $(c)~ \mathcal{L}\{e^{-at}\} = \frac{1}{s+a}$

# **Solution/Code**

# In[11]:


t, s, k, a, b, c  = sp.symbols('t s k a b c')
print('Output:\n')

# a
eq1_laplace = sp.laplace_transform(k,t,s)
display(a)
display(eq1_laplace[0])
print(' ')

# b
eq2_laplace = sp.laplace_transform(2*t,t,s)
display(b)
display(eq2_laplace[0])
print(' ')

# c
eq3_laplace = sp.laplace_transform(sp.exp(-a*t),t,s)
display(c)
display(eq3_laplace[0])


# **Problem 11.** Use the Laplace transform of the second derivative to derive
# 
# $~~~~~ \mathcal{L}\{cos~at\} = \frac{s}{s^2 + a^2}  $

# **Solution/Code**

# In[12]:


t, s = sp.symbols('t s')
print('Output:\n')

eq1 = sp.cos(a*t)
eq1_laplace = sp.laplace_transform(eq1,t,s)
display(eq1_laplace[0])


# ## **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;">1.4 The Initial and Final Value Theorems</span>**

#  -  The **initial value theorem** states:
# 
#     **$\lim_{t \to 0} f(t)$ $=$ $\lim_{s \to \infty} [s\mathcal{L} f(t)]$**
# 
# 
#  -  The **final value theorem** states:
# 
#     **$\lim_{t \to \infty} f(t)$ $=$ $\lim_{s \to 0} [s\mathcal{L} f(t)]$**
# 
# 
# <br/>

# **Problem 12.** Verify the initial value theorem for the voltage function $(5 + 2cos3t)$ volts, and state its initial value.

# **Solution/Code**

# In[16]:


t, s = sp.symbols('t s')
print('Output:\n')

eq1 = 5 + 2*sp.cos(3*t)
eq1_limit = sp.limit(eq1, t, 0)

eq1_laplace = sp.laplace_transform(eq1, t, s)
eq1_laplace_limit = sp.limit(s*eq1_laplace[0],s,oo)

print(f"{eq1_limit} = {eq1_laplace_limit}, which verifies the theorem in this case.")
print(f'\nThe initial value of the voltage is thus {eq1_limit}V.')


# **Problem 13.** Verify the initial value theorem function $(2t - 3)^2$ and state its initial value.

# **Solution/Code**

# In[14]:


t, s = sp.symbols('t s')
print('Output:\n')

eq1 = (2*t - 3)**2
eq1_limit = sp.limit(eq1, t, 0)

eq1_laplace = sp.laplace_transform(eq1, t, s)
eq1_laplace_limit = sp.limit(s*eq1_laplace[0],s,oo)

print(f"{eq1_limit} = {eq1_laplace_limit}, which verifies the theorem in this case.")
print(f'\nThe initial value of the given function is thus {eq1_limit}.')


# **Problem 14.** Verify the final value theorem for the function $(2 + 3e^{-2t}sin4t)cm$, which represents the displacement of a particle. State its final steady value.

# **Solution/Code**

# In[15]:


t, s = sp.symbols('t s')
print('Output:\n')

eq1 = 2 + 3*(sp.exp(-2*t))*sp.sin(4*t)
eq1_limit = sp.limit(eq1, t, oo)

eq1_laplace = sp.laplace_transform(eq1, t, s)
eq1_laplace_limit = sp.limit(s*eq1_laplace[0],s,0)

print(f"{eq1_limit} = {eq1_laplace_limit}, which verifies the theorem in this case.")
print(f'\nThe final value of the displacement is thus {eq1_limit}cm.')


# # **<span style="color: #3F819A; font-family: Times New Roman; font-size: 1.25em;">Summary</span>**
# 
# The Sympy library was used to to perform symbolic calculations. For this module which is about laplace transform, Sympy library contains modules necessary to perform laplace transform calculation. 
