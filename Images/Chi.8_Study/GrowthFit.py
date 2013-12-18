import IB
from PeristalticPumpGeometry2D import JaffrinMeanFlow

import pylab as m
import pickle

from pylab import log
from Fit import LinearRegression

from PlotUtility import *
StartLatex()

def DirectSearch(Range1, Range2, f, N=10.0, tol=.00001, output=False):
    PrevBest = None
    for i in range(100):
        if output: print Range1, Range2
        Width1 = Range1[1] - Range1[0]
        xs = m.arange(Range1[0], Range1[1] + Width1/N, Width1 / N)
        Width2 = Range2[1] - Range2[0]
        ys = m.arange(Range2[0], Range2[1] + Width2/N, Width2 / N)
        
        if abs(Width1) < tol or abs(Width2) < tol: return PrevBest
        
        Best, BestVal = (xs[0], ys[0]), f(xs[0], ys[0])
        for x in xs:
            for y in ys:
                val = f(x,y)
                if val < BestVal:
                    BestVal = val
                    Best = (x, y)
                    
        if Best == PrevBest or PrevBest!=None and abs(Best[0]-PrevBest[0])+abs(Best[1]-PrevBest[1])<.000001:
            Range1 = (Best[0] - Width1 / 4, Best[0] + Width1 / 4)
            Range2 = (Best[1] - Width2 / 4, Best[1] + Width2 / 4)
        else:
            Range1 = (Best[0] - Width1 / 2, Best[0] + Width1 / 2)
            Range2 = (Best[1] - Width2 / 2, Best[1] + Width2 / 2)
        PrevBest = Best
        
        if output: print BestVal, Best
    
    return Best
        
        



#Cs = m.arange(.85, .9, .0075)
#betas = m.arange(565, 575, .03)
#C2s = m.arange(-999, -1019, -1)
#def Fit(C, beta, C2):
    #return beta / (C - t) + C2
#BEST 16451.2120282 (0.87999999999999978, 569.01999999999634, -1013)

# Exponential-Plus model
#betas = m.arange(6.7, 6.85, .002)
#Cs = m.arange(18.5, 19.15, .005)
#C2s = m.arange(-100.0, -103, -.2)
#def Fit(C, beta, C2):
    #return C * m.exp(beta * t) + C2
#BEST 1430.84646506 (18.644999999999971, 6.8319999999999856, -102.0)

# Blowup model
#Cs = m.arange(193, 199, .125)
#betas = m.arange(5.5, 5.95, .0125)
#C2s = m.arange(1.32, 1.38, .00125)
#def Fit(C, beta, C2):
    #return C / (C2 - t)**beta
#BEST 78624.1696635 (198.625, 5.8875000000000055, 1.3637499999999991)

# Exponential model
betas = m.arange(7.2, 8, .001)
Cs = m.arange(9, 11, .0025)
C2s = [0]
def Fit(C, beta, C2):
    return C * m.exp(beta * t)
#BEST 16703.0662184 (10.000000000000313, 7.6779999999999031, 0)

def Error(C, beta, C2):
    fit = Fit(C, beta, C2)#beta / (C - t)
    error = (fit - sup)
    return m.dot(error, error)




picklefile = open('Chi.8.pkl', 'r')
Data = pickle.load(picklefile)
picklefile.close()



Ns = range(256, 2048+256, 256)
fits = []
for N in Ns:
    start, end = 30, 80
    start, end = 35, 70
    sup = m.array(Data[N]['sup_S_mid'][start:end])
    t = m.array(Data[N]['t'][start:end])
    
    fits.append(DirectSearch((0, 10), (0, 10), lambda x, y: Error(x, y, 0)))


# C vs N
m.clf()
Cs = m.array([fit[0] for fit in fits])
print Cs
#m.plot(Ns, Cs)
#m.xlabel(r'$N$', fontsize=18)
#m.plot(log(Ns), Cs)
LinearRegression(log(Ns), Cs)
m.plot(log(Ns), Cs, 'o', markersize=10)
m.xlabel(r'$\log N$', fontsize=18)
m.ylabel(r'$C$')
m.savefig('Chi.8GrowthFitVsN.png')

# \beta vs N
m.clf()
bs = m.array([fit[1] for fit in fits])
print bs
#m.plot(Ns, bs)
#m.xlabel(r'$N$', fontsize=18)
#m.plot(log(Ns), bs)
LinearRegression(log(Ns), bs)
m.plot(log(Ns), bs, 'o', markersize=10)
m.xlabel(r'$\log N$', fontsize=18)
m.ylabel(r'$\beta$')
m.savefig('Chi.8GrowthFitVsN_beta.png')

# C and \beta vs N
m.clf()
LinearRegression(log(Ns), Cs)
m.plot(log(Ns), Cs, 's', markersize=8, label='$C$')
LinearRegression(log(Ns), bs)
m.plot(log(Ns), bs, 'o', markersize=10, label='$\beta$')
m.xlabel(r'$\log N$', fontsize=18)
m.savefig('Chi.8GrowthFitVsN_C_beta.png')


# Fitted curve for N=2048
m.clf()
Best = fits[-1]
m.plot(t, sup, label='Simulation', lw=2)
#m.plot(t, Fit(Best[0], Best[1], Best[2]), '--', label='Fit', lw=2)
m.plot(t, Fit(Best[0], Best[1], 0), '--', label='Fit', lw=2)
m.xlabel(r'$t$', fontsize=18)
m.ylabel(r'$||\tilde{S}_{xx}||_\infty$')
m.legend(loc=2)
m.savefig('Chi.8GrowthFit_Exponential.png')
