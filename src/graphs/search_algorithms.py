"""This file contains functions for running graph algorithms
compatible with the UndirectedGraph class.
"""
from src.minimum_heap.min_heap import MinHeap # minimum heap for dijkstra
from src.graphs.search_graph import SearchGraph # for typing


def dijkstra(graph: SearchGraph, src: int) -> MinHeap:
    """Finds the shortest paths from a given graph and source Vertex
    using Dijkstra's Shortest Path algorithm.
    
    Returns None if given Vertex is invalid or not in graph.
    
    Args:
        graph: A SearchGraph.
        src: A source SearchItem index in the graph.
        
    Returns:
        A MinHeap with Vertices sorted by shortest path to longest.
    """
    # check if src in graph
    if src >= len(graph):
        return None
    # instantiate data strucutres for algorithm
    known = set()
    edge_to: dict[int, int] = {} # node path
    dist_to: dict[int, float] = {} # source distance
    # set starting distance
    dist_to[src] = 0
    # instantiate max heap
    result = MinHeap()
    min_heap = MinHeap()
    min_heap.add(src, dist_to[src])
    # find shortest paths
    while min_heap.size() > 0:
        u = min_heap.pop() # longest dist in queue
        known.add(u) # add to known
        if u in result:
            result.change_priority(u, dist_to[u])
        else:
            result.add(u, dist_to[u]) # add to results
        # traverse through edges
        for v, weight in graph.get_edges(u):
            old_dist = dist_to.get(v, float('inf'))
            new_dist = dist_to.get(u) + weight
            # ignore if new distance is longer than old
            if new_dist > old_dist:
                continue
            # update shortest path
            dist_to[v] = new_dist
            edge_to[v] = u
            # update min heap
            if v in min_heap:
                min_heap.change_priority(v, new_dist)
            else:
                min_heap.add(v, new_dist)
    return result