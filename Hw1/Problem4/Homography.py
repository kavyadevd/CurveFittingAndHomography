#!/usr/bin/env python
# coding: utf-8

# ### Homography and SVD computation

# In[29]:


import numpy as np
from numpy import linalg as LA


def SVD(A):     # returns VT,U,S = result of SVD
    A_At = A.transpose()
    # print(A_At)

    # Calculate A dot A transpose and A transpose dot A
    At_A = np.dot(A_At, A)
    #print("A_transpose.A = \n",At_A)
    A_At = np.dot(A,A_At)
    #print("A.A_transpose = \n",A_At)

    # GEt EIgen value and eigen vectors of A transpose dot A
    V_eigen_val, V_eigen_vec = LA.eig(At_A)
    # GEt EIgen value and eigen vectors of A dot A transpose
    U_eigen_val, U_eigen_vec = LA.eig(A_At)

    # Arrange eigen values and vectors in descending order for V
    V_eigen_val_ = V_eigen_val.argsort()[::-1]
    V_eigen_vec_ = V_eigen_vec[:, V_eigen_val_]
    V_eigen_vec_transpose = V_eigen_vec_.T



    # Arrange eigen values and vectors in descending order for U
    U_eigen_val_ = U_eigen_val.argsort()[::-1]
    U_eigen_vec_ = U_eigen_val[U_eigen_val_]
    U_eigen_vec__ = U_eigen_vec[:, U_eigen_val_]


    # Arrange elements for sigma
    U_diagonal_sqrt = np.diag((np.sqrt(U_eigen_vec_)))
    S = np.zeros_like(A).astype(np.float64)
    S[:U_diagonal_sqrt.shape[0], :U_diagonal_sqrt.shape[1]] = U_diagonal_sqrt


    # Compute H matrix from last column of V
    H = V_eigen_vec_[:, 8]
    H = np.reshape(H, (3, 3))

    return V_eigen_vec_transpose, U_eigen_vec__, S, H


# In[30]:


# Define points for matrix A
x1, x2, x3, x4 = 5, 150, 150, 5
y1, y2, y3, y4 = 5, 5, 150, 150
xp1, xp2, xp3, xp4 = 100, 200, 220, 100
yp1, yp2, yp3, yp4 = 100, 80, 80, 200


A = np.array([[-x1, -y1, -1, 0, 0, 0, x1*xp1, y1*xp1, xp1],     # Define matrix A for four points
              [0, 0, 0, -x1, -y1, -1, x1*yp1, y1*yp1, yp1],
              [-x2, -y2, -1, 0, 0, 0, x2*xp2, y2*xp2, xp2],
              [0, 0, 0, -x2, -y2, -1, x2*yp2, y2*yp2, yp2],
              [-x3, -y3, -1, 0, 0, 0, x3*xp3, y3*xp3, xp3],
              [0, 0, 0, -x3, -y3, -1, x3*yp3, y3*yp3, yp3],
              [-x4, -y4, -1, 0, 0, 0, x4*xp4, y4*xp4, xp4],
              [0, 0, 0, -x4, -y4, -1, x4*yp4, y4*yp4, yp4]])

#print("A=\n",np.mat(A))

VT, U, S, H = SVD(A)


# #### Matrix V

# In[31]:


print(VT.transpose())


# #### Matrix U

# In[32]:


print(U)


# #### Matrix $\Sigma$

# In[33]:


print(S)


# #### Homography Matrix

# In[34]:


print(H)

