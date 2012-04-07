"""The file contains the adjacency list representation of a simple undirected
graph. There are 40 vertices labeled 1 to 40. The first column in the file
represents the vertex label, and the particular row (other entries except the first column) tells all the
vertices that the vertex is adjacent to. So for example, the 6th row looks liks
: "6 29 32 37 27 16". This just means that the vertex with label 6 is adjacent
to (i.e., shares an edge with) the vertices with labels 29, 32, 37, 27 and 16.

Your task is to code up and run the randomized contraction algorithm for the min
cut problem and use it on the above graph to compute the min cut. (HINT: Note
that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you also think about more efficient implementations.)
"""

from string import split 
from random import randint
from copy import deepcopy

def min_cut (graph):
    """Returns the number of min cut of the graph using randomized contraction
    algorithm.
    """
    vertices = len(graph)
    if vertices == 2:
        return len(graph.values()[0])
    else:
        # choose a random vertex and random edge incident on it
        rnd_v_s = graph.keys()[randint(0, vertices - 1)] # one endpoint of the edge
        rnd_edge_index = randint(0, len(graph[rnd_v_s]) - 1)
        rnd_v_e = graph[rnd_v_s][rnd_edge_index] # the other endpoint
        # merge the two vertices into one and remove self loops
        graph[rnd_v_s] = [x for x in graph[rnd_v_s] + graph[rnd_v_e] if x != rnd_v_s and x !=
                          rnd_v_e]
        del graph[rnd_v_e] # delete the other endpoint
        # update other vetices
        for value in graph.values():
            value[:] = [x if x != rnd_v_e else rnd_v_s for x in value]
        return min_cut(graph)

# build the adjancent graph, where key is the vertex label and its value is a list
# of adjancent vertices
f = open('kargerAdj.txt')
graph = {}
for line in f:
    nums = split(line)
    graph[int(nums[0])] = map(int,nums[1:])
f.close()

# run the function n times and select the min
results = []
for i in range(40):
    results.append(min_cut(deepcopy(graph)))
print results, min(results)

