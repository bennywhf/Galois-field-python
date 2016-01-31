#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ebenezer.reyes
#
# Created:     09/01/2015
# Copyright:   (c) ebenezer.reyes 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from copy import *
from time import sleep
def xor(a,b):
    return (a + b) % 2

def polyadd(a,b):
    c = ['0']*len(a)
    for i in range(len(a)):
        c[i] = xor(a[i],b[i])
    return c

def polymul(a,b,p):
    c = [0] * (len(a)+1)
    ap = deepcopy(a)
    ap.insert(0,0)
    bp = deepcopy(b)
    bp.insert(0,0)
    index = len(ap) - 2
    if ap[-1] == 1:
        c = polyadd(c,bp)
    while(index != 0):
        index = index - 1
        bp.pop(0)
        bp.append(0)
        if bp[0] == 1:
            bp = polyadd(bp,p)
        if(a[index] == 1):
            c = polyadd(c,bp)
    return c[1:]

def nrpolymul(a,b):
    c = [0] * (len(a)+1)
    ap = deepcopy(a)
    ap.insert(0,0)
    bp = deepcopy(b)
    bp.insert(0,0)
    index = len(ap) - 2
    if ap[-1] == 1:
        c = polyadd(c,bp)
    while(index != 0):
        index = index - 1
        bp.pop(0)
        bp.append(0)
        if(a[index] == 1):
            c = polyadd(c,bp)
    return c[1:]

def polydiv(num,den):
    size = len(num)
    nump = deepcopy(num)
    denp = deepcopy(den)
    r = [0]*size

    if(nump == 0):
        raise Exception("division by zero")

    if(denp == r):
        return r

    while(True):
        try:
            if not(nump.index(1) <= denp.index(1)):
                break
        except Exception:
            break
        i =  denp.index(1) - nump.index(1)
        c = [0]*size
        c[-i - 1] = 1
        r = polyadd(c,r) #adding to quotient
        c = polymul(c,denp,[0]*(size+1))
        nump = polyadd(c,nump)
    return {'quotient':r,'remainder':nump}

def polyinverse(a,p):
    t = [0]*len(a)
    newt = deepcopy(t)
    newt[-1] = 1
    r = deepcopy(p)
    newr = deepcopy(a)

    while(newr != [0]*len(a)):
        if len(r) > len(newr): #first step of this algorithm will involve p as n+1 bits.
            newr.insert(0,0)
            quotient = polydiv(r,newr)['quotient']
            print(quotient)
            break
        else:
            quotient = polydiv(r,newr)['quotient']
            r,newr = deepcopy(newr),polyadd(r,polymul(quotient,newr,p))
            t,newt = deepcopy(newt),polyadd(t,polymul(quotient,newt,p))
            print(t,newt,r,newr)
    return(r,t)

def Madd(X1,Z1,X2,Z2,P):
    T1 = [0] * len(Z1) #1
    T1[-2] = 1
    X1 = polymul(X1,Z2,P)#2
    Z1 = polymul(Z1,X2,P)#3
    T2 = polymul()#4
    Z1 = polyadd(Z1,X1)#5
    Z1 = polymul(Z1,Z1,P)#6
    X1 = polymul(Z1,T1,P)
    X1 = polyadd(X1,T2)

def Mdouble(X,Z,P):
    T1 = [0] * len(Z1)
    T1 = polyadd(T1,c)
    X = polymul(X,X,P)
    Z = polymul(Z,Z,P)
    T1 = polymul(Z,T1,P)
    Z = polymul(A,X,P)
    T1 = polymul(T1,T1,P)
    X = polymul(X,X,P)
    X = polyadd(X,T1)

def Mxy(X1,Z1,X2,Z2):
    pass

def main():
    #print(polyadd([1,1,0,0],[0,1,0,1]))
    #print(polymul([0,1,0],[1,0,0],[1,1,0,1]))
    #print(polydiv([1,1,0,0],[0,1,1,0]))
    #print(polymul([1,1,1],[1,0,0],[1,0,1,1]))
    print(polyinverse([0,1,1],[1,0,1,1]))

if __name__ == '__main__':
    main()