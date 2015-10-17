__author__ = 'ThKiller'

import networkx as nx
import matplotlib.pyplot as plt
import operator
import collections
from itertools import chain, combinations
import math

def powerset(s):
  return [[s[j] for j in xrange(len(s)) if (i&(1<<j))] for i in xrange(1<<len(s))]

def powerset_generator(i):
    for subset in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
        yield set(subset)

def draw_graph(G):
     edges=nx.draw_networkx_edges(G,pos=nx.spring_layout(G))
     plt.show()
#nodes = ['s',0,1,2,3,4,5,6,7,8,9,10,'t']




nodes=['s','t','a','b','c','d','e','f','g','h']
edges_newcr=[('s','t'),('s','a'),('a','t'),('s','b'),('b','c'),('c','t') ]


edges_newcr1=[('a','c'),('b','c'),('c','t') ]
exo=('s','a'),('s','b')


edges_obexa=[('s','a'),('s','b'),('a','c'),('a','d'),('b','t')]
exo=[('c','t'), ('d','t')]

edgesarr=[('a','b'),('a','c'),('c','b')]

edgesnet=[('a','b'),('a','c'),('b','c'),('b','d'),('b','e'),('c','e'),('c','d'),('d','f'),('d','e'),('d','g'),('e','g'), ('e','f'),('f','g'),('f','h'),('g','h')]

result=dict()

##example 8.1

s='s'
t='t'
subgraphs=powerset_generator(edges_obexa)

#print(subgraphs)

for graphs in subgraphs:
    G=nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(exo)
    G.add_edges_from(graphs)
    #print(G.edges())
    if nx.has_path(G,s,t)==True:
        for edge in G.edges():
          if edge not in exo:
            G.remove_edge(*edge)
            if nx.has_path(G,s,t)==False:
               if edge in result.keys():
                 result[edge]=result[edge]+1
                 #print(edge)
                 #print(G.edges())
                 #nx.draw(G)
                 #plt.savefig("simple_path.png")
                 #plt.show()
               else:
                   result.update({edge:1})
            G.add_edge(*edge)
            if edge==('b', 'c'):
               print(G.edges())

    G.clear()

score=0.0
total=0.0
for key in result.keys():
    total=result[key]+total
for key in result.keys():
    score=(float(result[key])/total)
    score=round(score,2)
    result[key]=(result[key],score,)
actualcauses = collections.namedtuple('contibution', 'score edge')
explanation = sorted([actualcauses(v,k) for (k,v) in result.items()], reverse=True)

for top in explanation:
    print top

