"""
The file contains the edges of a directed graph. Vertices are labeled as
positive integers from 1 to 875714. Every row indicates an edge, the vertex
label in first column is the tail and the vertex label in second column is the
head (recall the graph is directed, and the edges are directed from the first
column vertex to the second column vertex). So for example, the 11th row looks
liks : "2 47646". This just means that the vertex with label 2 has an outgoing
edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing
strongly connected components (SCCs), and to run this algorithm on the given
graph. 

Output Format: You should output the sizes of the 5 largest SCCs in the given
graph, in decreasing order of sizes, separated by commas (avoid any spaces). So
if your algorithm computes the sizes of the five largest SCCs to be 500, 400,
300, 200 and 100, then your answer should be "500,400,300,200,100". If your
algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if
your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your
answer should be "400,300,100,0,0".
"""

from bitarray import bitarray
from bidict import bidict
import sys, resource

# remove the limit on stack size, but it requires sudo
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
# set the maximum recursion depth, the default is 1000, not enough for this
sys.setrecursionlimit(1000000)

def get_f_time(graph_rev, num_of_nodes):
  """Return finishing time for all nodes"""
  get_f_time.t = 0
  def dfs(v, f_time, explored):
    explored[v] = True
    for edge in graph_rev.get(v, []):
      if not explored[edge[1]]:
        dfs(edge[1], f_time, explored)
    get_f_time.t += 1
    f_time[v] = get_f_time.t

  global explored
  explored.setall(False)
  f_time = bidict() # bi-directional mapping from vertext to finishing time
  for v in range(num_of_nodes, 0, -1):
    if not explored[v]: 
      dfs(v, f_time, explored)
  return f_time

def compute_scc(graph, f_time):
  """Return a dict with mappings from the leader of a SCC to the SCC's size"""
  def dfs(v, leader, leaders, explored):
    explored[v] = True
    leaders[leader] = leaders.get(leader, 0) + 1
    for edge in graph.get(v, []):
      if not explored[edge[1]]:
        dfs(edge[1], leader, leaders, explored)

  global explored
  explored.setall(False)
  leaders = {} # mappings from leader to the size of its SCC
  s = None # vertex from which the last DFS call was invoked
  # process vertices in decreasing order of f_time
  for fin in sorted(f_time.values(), reverse=True):
    v = f_time[:fin] # get vertex 
    if not explored[v]:
      s = v
      dfs(v, s, leaders, explored)
  return leaders

#build graph using adjacency list, each edge is a 2-tuple
graph = {}
graph_rev = {} # graph with all arcs reversed
num_of_nodes = 0
if len(sys.argv) < 2:
  print 'Format: ./[this script name] [data file name]'
  sys.exit(0)
f = open(sys.argv[1])
for line in f:
  edge = map(int, line.split())
  graph.setdefault(edge[0], []).append((edge[0], edge[1]))
  graph_rev.setdefault(edge[1], []).append((edge[1], edge[0]))
  num_of_nodes = max(num_of_nodes, edge[0], edge[1])
f.close()

explored = bitarray(num_of_nodes + 1) # 0 is not used
f_time = get_f_time(graph_rev, num_of_nodes)
leaders = compute_scc(graph, f_time)
print sorted(leaders.values(), reverse=True)[:5]
