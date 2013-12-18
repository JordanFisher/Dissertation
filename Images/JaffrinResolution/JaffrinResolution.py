import IB
from PeristalticPumpGeometry2D import JaffrinMeanFlow

import pylab as m
import pickle

from PlotUtility import *
StartLatex()

import cwd; cwd.SetWdTo(__file__)

picklefile = open('JaffrinResolution.pkl', 'r')
Data = pickle.load(picklefile)
picklefile.close()

Chis = m.arange(.05, 1, .1)

# Simulated Jaffrins at different points in time (should all be the same)
def FullJaffrinSettled():
    m.clf()

    Jaffrin =  JaffrinMeanFlow(Chis, 1.5)
    m.plot(Chis, Jaffrin, 'g--', label='Jaffrin', lw=2)

    N = 1024
    for T in [120, 150, 180]:
        l = [Data[(0, '%g'%Chi, N)]['meanflow'][T] for Chi in Chis]
        m.plot(Chis, l, label='T = %g' % Data[(0, '%g'%Chi, N)]['t'][T])
    
    m.legend(loc=2)
    m.xlabel(r'$\chi$', fontsize=18)
    m.ylabel(r'$\Theta$')
    SetTickFont()
    
    m.savefig('JaffrinSettled.png')


# Newtonian Jaffrins curve
def FlowVsChi():
    m.clf()

    Jaffrin =  JaffrinMeanFlow(Chis, 1.5)
    m.plot(Chis, Jaffrin, 'g--', label='Jaffrin', lw=2)

    for N in [256, 512, 1024]:
    #for N in range(256, 2048+256, 256):
        #print N, [Data[(0, '%g'%Chi, N)]['t'][-1] for Chi in Chis]
    #raise
        l = [Data[(0, '%g'%Chi, N)]['meanflow'][150] for Chi in Chis]
        m.plot(Chis, l, label='$N = %i$'%N)
    
    m.legend(loc=2)
    m.xlabel(r'$\chi$', fontsize=18)
    m.ylabel(r'$\Theta$')
    SetTickFont()
    
    m.savefig('JaffrinVsChi.png')

def FlowVsN(Chi):
    m.clf()

    j = JaffrinMeanFlow(Chi, 1.5)
    m.plot([256, 1280], [j, j], label='Jaffrin', lw=2)
    
    Ns = range(256, 1280+256, 256)
    l = [Data[(0, '%g'%Chi, N)]['meanflow'][120] for N in Ns]
    
    m.plot(Ns, l, label='Simulated')
    m.plot(Ns, l, 'o')
    
    m.legend(loc=6)
    m.xlabel(r'$N$', fontsize=18)
    m.ylabel(r'$\Theta$')
    SetTickFont()
    
    m.savefig('JaffrinVsN_Chi%g.png' % Chi)

FullJaffrinSettled()
#FlowVsChi()
#FlowVsN(.35)
#FlowVsN(.85)