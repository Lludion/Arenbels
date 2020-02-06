
import numpy as np
import matplotlib.pyplot as plt
from arenbels.tools.wrap import wrap

def plot_show(*args,**kwargs):
    plt.legend(loc="best")
    plt.show()

def plot_hist(c,spec,label):
    plt.plot(c.get_history()[:,spec:spec+1],label=label)

def plot_named(stat,name,info,spec):
    """ plot of charasteritics of one named entity """
    if stat.name == name:#If it is the right entity :
        if spec is not None:
            spec %= len(info)
            plt.ylabel(info[spec])
            plot_hist(stat,spec,stat.name)
        else:
            for spec_i in range(len(info)):
                plot_hist(stat,spec_i,info[spec_i])

def preplot_unnamed(info,spec):
    """ all the work before the plot_hist is done here (for unnamed plots)"""
    if spec is None:
        spec = 0
    spec %= len(info)
    plt.ylabel(info[spec])
    return spec

@wrap(post=plot_show)
def city(g,name=None,spec=None,comp=False,begin=0,end=None):
    """ g is a game
    name is the name of the city you wnat to study.
    spec is the name of the parameter you want to study cities on
    comp is a couple of names : the two cities you want to compare (WiP)
    begin is the number of the first studied turn (by default : 0)
    end is the number of the last studied turn (by default : game.turn)
    """
    if end is None:
        end = g.turn
    plt.xlabel('Turn')
    if name is None:
        spec = preplot_unnamed(g.city_info,spec)
        for p in g.players:
            for c in p.state.cities:
                plot_hist(c,spec,c.name)
        plt.legend(loc="best")
        plt.show()
    else:
        for p in g.players:
            for c in p.state.cities:
                plot_named(c,name,g.city_info,spec)

@wrap(post=plot_show)
def state(g,name=None,spec=None,comp=False,begin=0,end=None):
    if end is None:
        end = g.turn
    plt.xlabel('Turn')
    if name is None:
        spec = preplot_unnamed(g.state_info,spec)
        for p in g.players:
            plot_hist(p.state,spec,p.state.name)
    else:
        for p in g.players:
            plot_named(p.state,name,g.state_info,spec)
