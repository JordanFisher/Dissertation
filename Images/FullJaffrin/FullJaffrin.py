import IB
from PeristalticPumpGeometry2D import JaffrinMeanFlow

import pylab as m
from EzPickle import *

from PlotUtility import *
StartLatex()


import cwd; cwd.SetWdTo(__file__)

#Data = Unpickle('FullJaffrin.pkl')
Data512 = Unpickle('FullJaffrin512.pkl')
#Data512_Old = Unpickle('FullJaffrin512_Old.pkl')

Ws = [1, 2, 5, 25, 55, 105]
wSymbol = { 1:'o', 2: '<', 5:'^', 15 :'>', 25 : 'p', 55:'s', 105:'D', 0:'*' }
#Ws = [1, 5, 55, 105]
#wSymbol = { 1:'o', 5:'^', 55:'s', 105:'D', 0:'*' }
Chis = m.arange(.05, .8, .05)
#Chis = m.arange(.05, .6, .1)

# Correct for corruption
W = 5
for Chi in m.arange(.1, .8, .1):
    data = Data512[(W, '%g'%Chi)]
    step = data['t'].index(8)
    print len(data['t']), data['t'][step-1:step+2]
    data['t'] = m.concatenate((m.zeros(799,m.float64), data['t'][step:]))
    data['meanflow'] = m.concatenate((m.zeros(799,m.float64), data['meanflow'][step:]))
    data['flow'] = m.concatenate((m.zeros(799,m.float64), data['flow'][step:]))
    print len(data['t']), data['t'][step-1:step+2]

Chi1 =      [     .05,     .10,     .15,     .20,     .25,     .30,     .35,    .40,     .45,     .50,     .55,     .60,     .65,     .70,     .75,     .80,     .85,     .90,    .95]
MeanFlow1 = [0.121335,0.237216,0.340324,0.434742,0.516466,0.585615,0.643237,0.69096,0.730879,0.764252,0.792879,0.818116,0.841197,0.863008,0.884246,0.905697,0.927845,0.951138,0.97486]

# Newtonian Jaffrins curve
def Newtonian():
    m.clf()
    
    m.plot(Chi1, MeanFlow1, 'b--')#, label='Simulated')
    m.plot(Chi1, MeanFlow1, 'bo', markersize=8, label='Simulated')
    
    Jaffrin =  JaffrinMeanFlow(Chi1, 1.5)
    m.plot(Chi1, Jaffrin, 'g--', label='Jaffrin \& Shapiro')
    m.legend(loc=2)

    xlatex(r'\chi')
    ylatex(r'\Theta')
    SetTickFont()
    
    m.savefig('Jaffrin.png')

def FullJaffrinTimeSlice(Frame, ws=Ws):
    _FullJaffrinTimeSlice(lambda w: Frame, '%i' % Frame, ws)
def FullJaffrinVariableTimeSlice(Frame, SaveAs, ws=Ws):
    _FullJaffrinTimeSlice(Frame, SaveAs, ws)
def _FullJaffrinTimeSlice(Frame, SaveAs, ws=Ws):
    m.clf()
    m.plot(Chi1, MeanFlow1, lw=2, label='Newtonian')
    #m.plot(Chi1[-4], MeanFlow1[-4], lw=2, label='Newtonian')
    
    for W in ws:
        frame = 101 if W == 0 else Frame(W)
        l = []
        for Chi in Chis:
            d = Data512[(W, '%g'%Chi)]
            l.append(d['meanflow'][frame-1])

        m.plot(Chis[:len(l)], l, wSymbol[W]+'-', label='$We=%g$'%W)
        #m.plot(Chis[:len(l)], l)
        
    xlatex(r'\chi')
    ylatex(r'\Theta')
    SetTickFont()
    #m.legend(loc=2)
    m.legend(loc=4)
    m.xlim(.05, .8)
    m.savefig('FullJaffrinVerbose_%s.png' % SaveAs)

def FullJaffrinAllTime(Chi, T1=1, T2=50, ws=Ws):
    m.clf()
    
    step1, step2 = T1*100+1, T2*100
    
    j = JaffrinMeanFlow(Chi, 1.5)
    m.plot([T1, T2], [j, j], label='J \& S', lw=2)
    
    #for W in [5, 55, 105]:
    for W in ws:
        d = Data512[(W, '%g'%Chi)]
        m.plot(d['t'][step1:step2], d['meanflow'][step1:step2], label='$We=%g$'%W)
        #m.plot(d['t'], d['flow'], label='$We=%g$'%W)
        
    xlatex(r't')
    ylatex(r'\Theta')
    SetTickFont()
    m.legend(loc=1)
    m.savefig('FullJaffrinOverTime_Chi%g.png' % Chi)

#Newtonian()    
    
FullJaffrinTimeSlice(850)
FullJaffrinTimeSlice(1500)
FullJaffrinTimeSlice(5000)

#FullJaffrinAllTime(.45, T2=50, ws=[5,55,105])
#FullJaffrinAllTime(.65, T2=50, ws=[5,55,105])

#FullJaffrinAllTime(.4, T1=10,T2=150, ws=[5,25,55,105])
#FullJaffrinAllTime(.6, T1=10,T2=150, ws=[5,25,55,105])
#FullJaffrinAllTime(.7, T1=10,T2=150, ws=[5,25,55,105])




## Alternative convective schemes
#Ws = [0, 5, 55]
#Chis = m.arange(.05, .8, .1)

#m.clf()

#Jaffrin =  JaffrinMeanFlow(Chi1, 1.5)
#m.plot(Chi1, Jaffrin, 'g--', label='Jaffrins')

#for W in Ws:
    #frame = 101 if W == 0 else 101
    #l = [Data[(W, '%g'%Chi, 'Centered_nu0')]['meanflow'][frame] for Chi in Chis]
    #m.plot(Chis, l, label='W=%g'%W)

    #l = [Data[(W, '%g'%Chi)]['meanflow'][frame] for Chi in Chis]
    #m.plot(Chis, l, '--', label='W=%g'%W)

#xlatex(r'\chi')
#ylatex(r'\Theta')    
#m.legend(loc=2)
#m.savefig('FullJaffrin_Centered.png')