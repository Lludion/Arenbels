
import numpy as np
import matplotlib.pyplot as plt



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
        if spec is None:
            spec = 0
        spec %= len(g.city_info)
        plt.ylabel(g.city_info[spec])
        for p in g.players:
            for c in p.state.cities:
                plt.plot(c.get_history()[:,spec:spec+1],label=c.name)

            plt.legend(loc="best")
            plt.show()
    else:
        for p in g.players:
            for c in p.state.cities:
                if c.name == name:
                    if spec is not None:
                        spec %= len(g.city_info)
                        plt.ylabel(g.city_info[spec])
                        plt.plot(c.get_history()[:,spec:spec+1],label=c.name)
                    else:
                        for spec_i in range(len(g.city_info)):
                            plt.plot(c.get_history()[:,spec_i:spec_i+1],label=g.city_info[spec_i])



        plt.legend(loc="best")
        plt.show()
