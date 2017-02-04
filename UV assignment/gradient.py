# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:49:21 2016

@author: Gunjan
"""

#UV DECOMPOSITION USING GRADIENT DESCENT AND VARIANTS
import math
import numpy

def RMSE(M,P):
    k = 0
    s = 0
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            if M[i][j] != 0:
                s = s + (M[i][j] - P[i][j])**2
                
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            if M[i][j] != 0:
                k = k + 1
    r = math.sqrt(s/k)

    return r
    
    
# UV decomposition using gradient descent !
def UVD(R, U, V, K, steps = 5000, alpha = 0.0002):
    V = V.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] != 0:  #defining the unknown terms as zero here.
                    eij = R[i][j] - numpy.dot(U[i,:],V[:,j])
                    for k in range(K):
                        U[i][k] = U[i][k] + alpha * 2 * eij * V[k][j] #updating U
                        V[k][j] = V[k][j] + alpha * 2 * eij * U[i][k] #updating V
    nR = numpy.dot(U,V)
    Rmse = RMSE(R, nR)
    print("For UVD using Gradient Descent : The root mean Square after", steps, "iterations is :", Rmse)
    return U, V.T
    
'''
        Regularization term 'beta' is added to avoid over-fitting. 
        beta is used to control the magnitudes of the user-feature and 
        item-feature vectors such that P and Q would give a good approximation
        of R without having to contain large numbers
'''

def UVD_withRegularizer(R, U, V, K, steps=5000, alpha=0.0002, beta=0.02):
    V = V.T #transpose
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] != 0:
                    eij = R[i][j] - numpy.dot(U[i,:],V[:,j])
                    for k in range(K):
                        U[i][k] = U[i][k] + alpha * (2 * eij * V[k][j] - beta * U[i][k]) #updating U
                        V[k][j] = V[k][j] + alpha * (2 * eij * U[i][k] - beta * V[k][j]) #updating V
    #there will be a change in the formula for RMSE due the presence of the 
    #regularization term 'beta'
    e = 0
    k = 0
    #first calculating sum of squares error
    for i in range(len(R)):
        for j in range(len(R[i])):
            if R[i][j] > 0:
                e = e + pow(R[i][j] - numpy.dot(U[i,:],V[:,j]), 2)
                for k in range(K):
                    e = e + (beta/2) * (pow(U[i][k],2) + pow(V[k][j],2))
    #now calculating root mean square error
    for i in range(0,len(R)):
        for j in range(0,len(R[i])):
            if R[i][j] != 0:
                k = k + 1
    r = math.sqrt(e/k)
    print("For UVD with regularizer 'beta' : The root mean Square after", steps, "iterations is :", r)
    return U, V.T

def main(R):
    
    R = numpy.array(R)
    N = len(R)
    M = len(R[0])
    K = 2
    #randomly initializing U and V
    U = numpy.random.rand(N,K) 
    V = numpy.random.rand(M,K)
    nP,nQ = UVD(R,U,V,K)
    print("For UVD using Gradient Descent : M =", numpy.dot(nP,nQ.T))
    Pr, Qr = UVD_withRegularizer(R,U,V,K)
    print("For UVD using Gradient Descent with regularizer : M =", numpy.dot(Pr,Qr.T))

R = [[5,2,4,4,3],[3,1,2,4,1],[2,0,3,1,4],[2,5,4,3,5],[4,4,5,4,0]]
main(R)