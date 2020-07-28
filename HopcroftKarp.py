# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:51:10 2019

@author: xujingyu
"""
import collections

class HopcroftKarp(object):
    """
    Class used to implement `Hopcroft--Karp matching algorithm
    <https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm>`_
    """

    """
    Parameters
    ----------
    G : NetworkX graph
      Undirected bipartite graph
    Returns
    -------
    matches : dictionary
      The matching is returned as a dictionary, `matches`, such that
      ``matches[v] == w`` if node ``v`` is matched to node ``w``. Unmatched
      nodes do not occur as a key in mate.
    Notes
    -----
    This function is implemented with the `Hopcroft--Karp matching algorithm
    <https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm>`_ for
    bipartite graphs.
    References
    ----------
    .. [1] John E. Hopcroft and Richard M. Karp. "An n^{5 / 2} Algorithm for
       Maximum Matchings in Bipartite Graphs" In: **SIAM Journal of Computing**
       2.4 (1973), pp. 225--231. <https://dx.doi.org/10.1137/0202019>.
    """
    INFINITY = -1

    def __init__(self, G, left_nodes):
        """
        Parameters
        ----------
        G : NetworkX graph
        Undirected bipartite graph
        left_nodes: Networkx bipartite set
        The nodes present on the left set of the bipartite graph `G`.
        """
        self.G = G
        self.left_nodes = left_nodes
        self.count = 0

    def match(self):
        """
        Returns maximal matching using the Hopcroft-Karp Algorithm.
        Returns
        -------
        self.match : dictionary
        The matching is returned as a dictionary, `self.match`, such that
        ``self.match[u] == v`` if node ``u`` is matched to node ``v`` or
        ``self.match[u] == None`` if node is unmatched.
        References
        ----------
        .. [1] John E. Hopcroft and Richard M. Karp. "An n^{5 / 2} Algorithm for
        Maximum Matchings in Bipartite Graphs" In: **SIAM Journal of Computing**
        2.4 (1973), pp. 225--231. <https://dx.doi.org/10.1137/0202019>.
        """
        self.N1 = self.left_nodes
        self.N2 = set(self.G.node) - self.left_nodes
        self.match = {}
        self.dist = {}
        self.q = collections.deque()

        #init
        for v in self.G:
            self.match[v] = None
            self.dist[v] = HopcroftKarp.INFINITY

        matching = 0

        while self.bfs():
            for v in self.N1:
                if self.match[v] is None and self.dfs(v):
                    matching = matching + 1

        # print("Pair: ", self.match)
        return self.match

    def dfs(self, v, all=False):
        if v != None:
            for u in self.G.neighbors(v):
                if self.dist[ self.match[u] ] == self.dist[v] + 1 and self.dfs(self.match[u]):
                    self.match[u] = v
                    self.match[v] = u
                    if all and u < 0:
                        self.candidates.add(u)
                    return True

            self.dist[v] = HopcroftKarp.INFINITY
            return False

        return True

    def bfs(self):
        for v in self.N1:
            if self.match[v] == None:
                self.dist[v] = 0
                self.q.append(v)
            else:
                self.dist[v] = HopcroftKarp.INFINITY

        self.dist[None] = HopcroftKarp.INFINITY

        while len(self.q) > 0:
            v = self.q.popleft()
            if v != None:
                for u in self.G.neighbors(v):
                    if self.dist[ self.match[u] ] == HopcroftKarp.INFINITY:
                        self.dist[ self.match[u] ] = self.dist[v] + 1
                        self.q.append(self.match[u])

        return self.dist[None] != HopcroftKarp.INFINITY