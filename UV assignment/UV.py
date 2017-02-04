# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:44:37 2016

@author: Gunjan
"""
#UV
import math

def SOS(M,P):
    s = 0
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            if M[i][j] != 0:
                s = s + (M[i][j] - P[i][j])**2

    return s

def RMSE(M,P):
    k = 0
    s = SOS(M,P)
    for i in range(0,len(M)):
        for j in range(0,len(M[i])):
            if M[i][j] != 0:
                k = k + 1
    r = math.sqrt(s/k)

    return r

def multiply(A,B):
    m = len(A)
    n = len(A[0])
    p = len(B)
    q = len(B[0])

    result = [[0 for x in range(0,q)]for y in range(0,m)]
    if n!= p:
        print("Matrix Multiplication not possible")
        exit
    for i in range(0,m):
        for j in range(0,q):
            for k in range(0,n):
                result[i][j] += A[i][k]*B[k][j]
    return result

def UV(M):
    U = [[1 for i in range(0,2)]for j in range(0,5)]
    V = [[1 for i in range(0,5)]for j in range(0,2)]
    print("Initial U =", U)
    print("Initial V =", V)
    P = multiply(U,V)
    print("Initial P =", P)
    a = SOS(M,P)
    r2 = RMSE(M,P)
    print("Initial SOS =", a)
    print("Initial RMSE =", r2)
    for r in range(0,len(U)):
        for s in range(0,len(U[r])):
            #U[i][j] = x
            f = 0
            t = 0
            w = 0
            b = 0
            x = 0
            for j in range(0,len(M[r])):
                if M[r][j] != 0:
                    f += V[s][j]*M[r][j]
                    t += (V[s][j])**2
                    b += (V[s][j])
            for k in range(0,len(V)):
                if s != k:
                    w += U[r][k]*V[k][r]
            print("Iteration #", r + 1, " of U ::::")
            '''print(f)
            print(t)
            print(b)
                print(w)'''
            x += (f - b*w) / t
            #print(x)
            U[r][s] = x
    
                #print("U : ", U)
            P1 = multiply(U,V)
                #print("P = ", P1)
            a1 = SOS(M,P1)
            r1 = RMSE(M,P1)
            print("SOS  =", a1)
            print("RMSE =", r1)
            
    
    for r in range(0,len(V)):
        for s in range(0,len(V[r])):
            f = 0
            b = 0
            w = 0
            t = 0
            y = 0
        #V[i][j] = y
            for i in range(0,len(M)):
                if M[i][s] != 0:
                    f += U[i][r]*M[i][s]
                    t += (U[i][r])**2
                    b += (U[i][r])
            for k in range(0,len(V)):
                if r != k:
                    w += U[s][k]*V[k][s]
                print("Iteration #", r + 1, " of V ::::")
                '''print(f)
                print(t)
                print(b)
                print(w)'''
            y += (f - b*w) / t
            #print(y)
            V[r][s] = y

                #print("V : ", V)
            P1 = multiply(U,V)
                #print("P = ", P1)
            a1 = SOS(M,P1)
            r1 = RMSE(M,P1)
            print("SOS  =", a1)
            print("RMSE =", r1)
    print(P1)
        

M = [[5,2,4,4,3],[3,1,2,4,1],[2,0,3,1,4],[2,5,4,3,5],[4,4,5,4,0]]
UV(M)


