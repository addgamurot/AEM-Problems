# -*- coding: utf-8 -*-
"""Gamurot_M2-L1_Matrices&Determinants_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1114w6keu94GvIIAaKRjraq-gaUCCcHa-

<font size="5">***Instruction*: Expand Python Modules and Functions section first then run the code below to avoid NameError when running the code in the Solutions/Code section.**</font>

#**Python Modules and Functions**
-- compiled by addgamurot
"""

from sympy import *
from sympy import pretty_print as pp 
from sympy.interactive import printing
printing.init_printing(use_latex=True)

"""# **<center>Module 2 <center/>**
# <center> **Lesson 1: Theory of Matrices and Determinants** <center/>
Solving Problems about Matrices and Determinants using Python.

##**1.1 Addition, Subtraction and Multiplication of Matrices**

###**Problem 1.**
Add the matrices

(a) $\begin{pmatrix} 
2 & -1  \\
-7 & 4 
\end{pmatrix}  and \begin{pmatrix} 
-3 & 0  \\
7 & -4 
\end{pmatrix}$


 (b) $\begin{pmatrix} 
3 & 1 & -4 \\
4 & 3 & 1 \\
1 & 4 & -3 
\end{pmatrix} 
and \begin{pmatrix} 
2 & 7 & -5 \\
-2 & 1 & 0 \\
6 & 3 & 4 
\end{pmatrix}$

###**Solution/Code/Answer**
"""

# (a) Solution 
pp('(a)\n\t')
A = Matrix([[2, -1],[-7, 4]])
B = Matrix([[-3, 0],[7, -4]])

C = A + B
display(C)
pp('\n\t')

# (b) Solution 
pp('(b)\n\t')
D = Matrix([[3, 1, -4],[4, 3, 1],[1, 4, -3]])
E = Matrix([[2, 7, -5],[-2, 1, 0],[6, 3, 4]])
F = D + E
display(F)

"""###**Problem 2.**
Subtract

(a) $\begin{pmatrix} 
-3 & 0  \\
7 & -4 
\end{pmatrix}  from \begin{pmatrix} 
2 & -1  \\
-7 & 4 
\end{pmatrix}$

 (b) $\begin{pmatrix} 
2 & 7 & -5 \\
-2 & 1 & 0 \\
6 & 3 & 4  
\end{pmatrix}  from \begin{pmatrix} 
3 & 1 & -4 \\
4 & 3 & 1 \\
1 & 4 & -3
\end{pmatrix}$

###**Solution/Code/Answer**
"""

# (a) Solution 
pp('(a)\n\t')
A = Matrix([[-3, 0],[7, -4]])
B = Matrix([[2, -1],[-7, 4]])

C = B - A
display(C)

pp('\n\t')

# (b) Solution 
pp('(b)\n\t')
D = Matrix([[2, 7, -5],[-2, 1, 0],[6, 3, 4]])
E = Matrix([[3, 1, -4],[4, 3, 1],[1, 4, -3]])
F = E - D 
display(F)

"""###**Problem 3.**
If $A = \begin{pmatrix} 
-3 & 0  \\
7 & -4 
\end{pmatrix} $, 
$~B =  \begin{pmatrix} 
2 & -1  \\
-7 & 4
\end{pmatrix} $ and $
C = \begin{pmatrix} 
1 & 0  \\
-2 & -4
\end{pmatrix}$ find $2A - 3B + 4C$.

###**Solution/Code/Answer**
"""

# Solution 
A = Matrix([[-3, 0],[7, -4]])
B = Matrix([[2, -1],[-7, 4]])
C = Matrix([[1, 0],[-2, -4]])

# Let D = 2A - 3B + 4C
D = 2*A - 3*B + 4*C
D

"""###**Problem 4.**
If $A = \begin{pmatrix} 
2 & 3  \\
1 & -4 
\end{pmatrix} $and 
$
B = \begin{pmatrix} 
-5 & 7  \\
-3 & 4
\end{pmatrix}$ find $A \times B$.

###**Solution/Code/Answer**
"""

# Solution 
A = Matrix([[2, 3],[1, -4]])
B = Matrix([[-5, 7],[-3, 4]])

# Let A x B = D
D = A*B
D

"""###**Problem 5.**
Simplify 
$\begin{pmatrix} 
3 & 4 & 0 \\
-2 & 6 & -3 \\
7 & -4 & 1 
\end{pmatrix} 
\times \begin{pmatrix} 
2  \\
5  \\
-1  
\end{pmatrix}$

###**Solution/Code/Answer**
"""

# Solution
A = Matrix([[3, 4, 0],[-2, 6, -3],[7, -4, 1]])
B = Matrix([[2],[5],[-1]])

#Let A x B = D
D = A*B
D

"""###**Problem 6.**
If  $A = \begin{pmatrix} 
3 & 4 & 0 \\
-2 & 6 & -3 \\
7 & -4 & 1 
\end{pmatrix} $
and$~B = \begin{pmatrix} 
2 &-5  \\
5 & -6 \\
-1 & -7 
\end{pmatrix}$, find $A \times B$.

###**Solution/Code/Answer**
"""

# Solution
A = Matrix([[3, 4, 0],[-2, 6, -3],[7, -4, 1]])
B = Matrix([[2, -5],[5, -6],[-1, -7]])

#Let A x B = D
D = A*B
D

"""###**Problem 7.**
Determine
$\begin{pmatrix} 
1 & 0 & 3 \\
2 & 1 & 2 \\
1 & 3 & 1 
\end{pmatrix} 
\times \begin{pmatrix} 
2 & 2 & 0 \\
1 & 3 & 2 \\
3 & 2 & 0 
\end{pmatrix}$

###**Solution/Code/Answer**
"""

# Solution
A = Matrix([[1, 0, 3],[2, 1, 2],[1, 3, 1]])
B = Matrix([[2, 2, 0],[1, 3, 2],[3, 2, 0]])

#Let A x B = D
D = A*B
D

"""###**Problem 8.**
If $A = \begin{pmatrix} 
2 & 3  \\
1 & 0 
\end{pmatrix} $ and 
$
B = \begin{pmatrix} 
2 & 3  \\
0 & 1
\end{pmatrix}$ show that $A \times B \neq B \times A$.

###**Solution/Code/Answer**
"""

# Solution 
A = Matrix([[2, 3],[1, -4]])
B = Matrix([[-5, 7],[-3, 4]])

# Let A x B = D
pp('D\n\t')
D = A*B
display(D)
pp('\n\t')
# Let B x A = E
pp('E\n\t')
E = B*A
display(E)
pp('\n\t')
pp('Since D ≠ E, then A x B ≠ B x A')

"""##**1.2 The Determinant of a 2 x 2 Matrix**

###**Problem 9.**
Determine the value of 
$\begin{vmatrix}
3 & -2 \\
7 & 4
\end{vmatrix}
$

###**Solution/Code/Answer**
"""

# Let A be the determinant of the matrix
A = Matrix([[3, -2], [7, 4]])
print('A =', A.det())

"""###**Problem 10.**
Evaluate
$\begin{vmatrix}
(1 + j) & j2 \\
-j3 & (1-j4)
\end{vmatrix}$

###**Solution/Code/Answer**
"""

# Let A be the determinant of the matrix
z1 = 1 + 1j
z2 = 0 + 2j
z3 = 0 - 3j
z4 = 1 - 4j
A = Matrix([[z1, z2], [z3,z4]])
print('A =', A.det())

"""##**1.3 The Inverse Reciprocal of a 2 x 2 Matrix**

###**Problem 11.**
Determine the inverse of 
$\begin{pmatrix}
3 & -2 \\
7 & 4
\end{pmatrix}$

###**Solution/Code/Answer**
"""

# Let A be the inverse of the matrix
A = Matrix([[3, -2],[7, 4]])
A.inv()

"""##**1.4 The Determinant of a 3 x 3 Matrix**

###**Problem 12.**
Find the value of 
$
\begin{vmatrix}
3 & 4 & -1 \\
2 & 0 & 7 \\
1 & -3 & -2
\end{vmatrix}
$

###**Solution/Code/Answer**
"""

# Let B be the determinant of the matrix
A = Matrix([[3, 4, -1],[2, 0, 7],[1, -3, -2]])
B = A.det()
print('B =', B)

"""###**Problem 13.**
Evaluate
$
\begin{vmatrix}
1 & 4 & -3 \\
-5 & 2 & 6 \\
-1 & -4 & 2
\end{vmatrix}
$

###**Solution/Code/Answer**
"""

# Let B be the determinant of the matrix
A = Matrix([[1, 4, -3],[-5, 2, 6],[-1, -4, 2]])
B = A.det()
print('B =', B)

"""##**1.5 The Inverse Reciprocal of a 3 x 3 Matrix**

###**Problem 14.**
Determine the inverse of the matrix
$
\begin{pmatrix}
3 & 4 & -1 \\
2 & 0 & 7 \\
1 & -3 & -2
\end{pmatrix}
$

###**Solution/Code/Answer**
"""

# Let B be the inverse of the matrix
A = Matrix([[3, 4, -1],[2, 0, 7],[1, -3, -2]])
B = A.inv()
print('B\n\t')
display(B)

"""###**Problem 15.**
FInd the inverse of
$
\begin{pmatrix}
1 & 5 & -2 \\
3 & -1 & 4 \\
-3 & 6 & -7
\end{pmatrix}
$

###**Solution/Code/Answer**
"""

# Let B be the inverse of the matrix
A = Matrix([[1, 5, -2],[3, -1, 4],[-3, 6, -7]])
B = A.inv()
print('B\n\t')
display(B)

"""#Summary
<div align="justify"><font size="3">For this module, the sympy library is used to perform symbolic or algebraic calculations .In this lesson, which is about matrices and determinants, sympy contains functions necessary for matrix calculations . </font></div>   

---

#<center>$---$End of Module 2, Lesson 1$---$<center/>
"""