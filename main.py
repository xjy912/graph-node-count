# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 10:55:25 2019

@author: xujingyu
"""
import numpy as np
import networkx as nx
from HopcroftKarp import HopcroftKarp

N_sources = 0
N_sinks = 0
N_drivers = 0
N_internal_dilations = 0
N_external_dilations = 0

def source_number_count(adjacent_matrix):
    in_degree = adjacent_matrix.sum(axis=0)
    exist = (in_degree>0)*1
    factor = np.ones((in_degree.shape[1],1))
    res = np.dot(exist,factor)
    source_numbers = adjacent_matrix.shape[1] - res
    return source_numbers
    
def sink_number_count(adjacent_matrix):
    out_degree =  adjacent_matrix.sum(axis=1)
    exist = (out_degree>0)*1
    factor = np.ones((1,out_degree.shape[0]))
    res = np.dot(factor,exist)
    sink_numbers = adjacent_matrix.shape[0] - res
    return sink_numbers


G = nx.from_edgelist(CSN_Net)
left_nodes = set(n for n,d in G.nodes(data=True))
hp=HopcroftKarp(G,left_nodes)
matching = hp.match()
unmatched = set(x for x in matching.keys() if matching[x] is None)

adjacent_matrix = nx.to_numpy_matrix(G)
N_sources = source_number_count(adjacent_matrix)
N_sinks = sink_number_count(adjacent_matrix)
N_drivers = len(unmatched) + (G.number_of_nodes() - len(unmatched))/2

N_external_dilations = N_sinks - N_sources
N_internal_dilations = N_drivers - N_sources - N_external_dilations
#==============================================================================
# def source_number_count(A):
#     sources_numbers = 0
#     for i in range (len(A)):
#         if(i>=1 and A[i,0]==A[i-1,0]): continue
#     for j in range(len(A)):
#         if(A[i,0]==A[j,1]): break
#         if(j==len(A)-1): sources_numbers+=1    #sources only appear in the first collumn
#     return sources_numbers
#     
# def sink_number_count(A):
#     sink_numbers = 0
#     for o in range(len(A)):
#         for m in range(o-1):
#             if(A[o,1]==A[m,1]):  break
#         for p in range(len(A)):
#             if(A[o,1]==A[p,0]): break
#             if(p==len(A)-1):  sink_numbers+=1   #sinks only appear in the second collumn  
#     return sink_numbers
#==============================================================================

#==============================================================================
# A = np.mat(CSN_Net)
# left_nodes = set(np.asarray(A[:,0]).ravel())
# right_nodes = set(np.asarray(A[:,1]).ravel())
# totol_nodes = left_nodes|right_nodes
#==============================================================================
#import time
#==============================================================================
# 
# def test_maximum_matching_fraction(g):
#     start_time = time.process_time()
#     d_nodes = maximum_matching_driver_nodes(g)
#     end_time = time.process_time()
# #     print("Code time: {}".format(end_time-start_time))
# #     return end_time-start_time
#     return len(d_nodes)/len(g.nodes)
#==============================================================================
