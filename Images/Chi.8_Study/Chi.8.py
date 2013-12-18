import IB
from PeristalticPumpGeometry2D import JaffrinMeanFlow

import pylab as m
import pickle

from pylab import log

from PlotUtility import *
StartLatex()


picklefile = open('Chi.8.pkl', 'r')
Data = pickle.load(picklefile)
picklefile.close()

Ns = range(256, 2048+256, 256)

#m.clf()
#for N in Ns:#[256, 1024, 1536, 2048]:
    #flow = Data[N]['flow'][10:130]
    #t = Data[N]['t'][10:130]
    #m.plot(t, flow, label='%g'%N)
    #m.xlabel(r't')
    #m.ylabel(r'\theta')
    #m.legend(loc=1)
#m.savefig('Chi.8_flows.png')
    

#m.clf()
#flow_compare = m.array(Data[2048]['flow'][10:100])
#for N in Ns:#[256, 1024, 1536, 2048]:
    #flow = m.array(Data[N]['flow'][10:100])
    #t = Data[N]['t'][10:100]
    #rel = (flow - flow_compare)
    #m.plot(t, rel, label='%g'%N)
#m.xlabel(r'$t$')
#m.ylabel(r'$\Q_N - \Q_{2048}$')
#m.legend(loc=1)
#SetTickFont()
#m.savefig('Chi.8_flows_rel.png')

m.clf()
for N in Ns:#[256, 1024, 1536, 2048]:
    sup = Data[N]['sup_S_mid'][:150]
    t = Data[N]['t'][:150]
    m.plot(t, sup, label='%g'%N)
m.xlabel(r'$t$', fontsize=18)
m.ylabel(r'$||\tilde{S}_{xx}||_\infty$')
m.legend(loc=2)
m.savefig('Chi.8_supmid.png')


m.clf()
sup = [Data[N]['sup_S_mid'][125] for N in Ns]
midy = (sup[0] + sup[-1]) / 2
midx = (log(Ns[0]) + log(Ns[-1])) / 2
slope = (sup[-1] - sup[0]) / (log(Ns[-1]) - log(Ns[0]))
m.plot(log(Ns), slope * (m.array(log(Ns)) - midx) + midy, '--', lw=2)
m.plot(log(Ns), sup, 'o', markersize=10)
print "slope =", slope
m.xlabel(r'$-\log h$', fontsize=18)
m.ylabel(r'$||\tilde{S}_{xx}||_\infty$')
m.savefig('Chi.8_T1.25_log.png')


#m.clf()
#sup = [Data[N]['sup_S_mid'][125] for N in Ns]
#m.plot(log(Ns), log(sup))
#midy = (log(sup[0]) + log(sup[-1])) / 2
#midx = .5*(log(Ns[0]) + log(Ns[-1])) / 2
#m.plot(log(Ns), .5 * m.array(log(Ns)) - midx + midy, '--')
#m.xlabel(r'\log N')
#m.ylabel(r'\log||\tilde{S}_xx||_\inf')
#m.savefig('Chi.8_T1.25_log.png')


#m.clf()
#MeanFlows = [Data[N]['flow'][101] for N in Ns]
#m.plot(Ns, MeanFlows, 'o', label='flow')
#m.xlabel(r'N')
#m.ylabel(r'\theta')
#m.savefig('ResolutionStudy_flow_vs_N.png')

#m.clf()
#sup_S = [Data[N]['sup_S'][101] for N in Ns]
#m.plot(Ns, sup_S, '*', label='||S_xx||_\inf')
#m.xlabel(r'N')
#m.ylabel(r'||S_xx||_\inf')
#m.savefig('ResolutionStudy_supS_vs_N.png')