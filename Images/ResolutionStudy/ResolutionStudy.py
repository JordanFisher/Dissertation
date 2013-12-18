import IB
from PeristalticPumpGeometry2D import JaffrinMeanFlow

import pylab as m
import pickle
from pylab import log

from PlotUtility import *
StartLatex()

import cwd; cwd.SetWdTo(__file__)

from Fit import LinearRegression


picklefile = open('ResolutionStudy.pkl', 'r')
Data = pickle.load(picklefile)
picklefile.close()

Ns = range(256, 2048+256, 256)

#m.clf()
#for N in [256, 1024, 1536, 2048]:
    #flow = Data[N]['flow'][65:85]#[:101]
    #t = Data[N]['t'][65:85]#:101]
    #m.plot(t, flow, label='%g'%N)
    #m.xlabel(r't')
    #m.ylabel(r'\theta')
    #m.legend(loc=1)
#m.savefig('ResolutionStudy_flows.png')
    

m.clf()
MeanFlows = m.array([Data[N]['flow'][101] for N in Ns])
print MeanFlows
raise
x = log(Ns)[:-2]
y = log(abs(MeanFlows - MeanFlows[-1]))[:-2]
m.plot(x, y, 'o', label='flow', markersize=8)
#Line(x[:], y[:])#, slope=-1)
LinearRegression(x, y)
m.xlabel(r'$-\log h$', fontsize=18)
m.ylabel(r'$\log error$', fontsize=18)
SetTickFont()
m.savefig('ResolutionStudy_flow_vs_N_log.png')

m.clf()
sup_S = m.array([Data[N]['sup_S'][101] for N in Ns])
x, y = log(Ns)[:-2], log(abs(sup_S - sup_S[-1]))[:-2]
m.plot(x, y, 'o', label='||S_xx||_\inf', markersize=8)
#Line(x[:], y[:])#, slope=-1)
LinearRegression(x, y)
m.xlabel(r'$-\log h$', fontsize=18)
m.ylabel(r'$\log error$', fontsize=18)
SetTickFont()
m.savefig('ResolutionStudy_supS_vs_N_log.png')

#m.clf()
#MeanFlows = [Data[N]['flow'][101] for N in Ns]
#m.plot(Ns, MeanFlows, 'x', label='flow')
#m.xlabel(r'N')
#m.ylabel(r'\theta')
#m.savefig('ResolutionStudy_flow_vs_N.png')

#m.clf()
#sup_S = [Data[N]['sup_S'][101] for N in Ns]
#m.plot(Ns, sup_S, '*', label='||S_xx||_\inf', )
#m.xlabel(r'N')
#m.ylabel(r'||S_xx||_\inf')
#m.savefig('ResolutionStudy_supS_vs_N.png')