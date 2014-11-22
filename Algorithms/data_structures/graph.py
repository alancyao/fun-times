class Edge:
  def __init__(self, u, v, weight):
    self.u = u
    self.v = v
    self.weight = weight

  def __str__(self):
    return "Edge from {} to {} with weight {}".format(u, v, w)

class Vertex:
  def __init__(self, item=None):
    self.item = item
    self.neighbors = {}
    self.degree = 0

  def addNeighbor(self, edge):
    self.degree += 1
    if edge.u is self:
      self.neighbors[edge.v] = edge
    else:
      self.neighbors[edge.u] = edge

  def neighbors(self):
    return self.neighbors.keys()

  def adjacent_edges(self):
    return self.neighbors.values()

  def adjacent(self):
    return self.neighbors.items()

  def remove_edge(self, v):
    del self.neighbors[v]
    self.degree -= 1

  def __str__(self):
    return "Vertex {}".format(self.item)

  def __cmp__(self, other):
    return self.item.__cmp__(other.item)

  def __lt__(self, other):
    return self.item.__lt__(other.item)

class Graph:
  def __init__(self):
    self.vertices = {}
    self.edges = set()
    self.N = 0

  def __str__(self):
    return "Graph with vertices: {} \n and edges: {} \n".format(
        self.vertices, self.edges)

  """ Adds a lone vertex """
  def add_vertex(self, item):
    v = Vertex(item)
    self.vertices[v] = None
    self.N += 1
    return v

  def add_edge(self, u, v, weight=1):
    if u not in self.vertices or v not in self.vertices:
      return None
    e = Edge(u, v, weight)
    if e not in self.edges:
      self.edges.add(e)
      u.addNeighbor(e)
      v.addNeighbor(e)

  def remove_edge(self, edge):
    if edge in self.edges:
      self.edges.remove(edge)
      edge.u.remove_edge(v)
      edge.v.remove_edge(u)

  def remove_vertex(self, v):
    if v in self.vertices:
      self.N -= 1
      del self.vertices[v]
      for e in v.adjacent_edges():
        self.remove_edge(e)

def explore(G, s, fringe_type=list, pop_func=list.pop,
            heuristic=lambda x: 0, distance_func=lambda x,y,z: 0,
            visit_func=lambda v: None):
  if s not in G.vertices:
    return
  fringe = fringe_type()
  visited = set()
  fringe.append((0, s))
  while fringe:
    dist, u = pop_func(fringe)
    if u in visited:
      continue
    visit_func(u)
    visited.add(u)
    for v, e in u.adjacent():
      fringe.append((heuristic(v)+distance_func(dist, u, e.weight), v))

def dfs(G, s, visit_func=lambda v: None):
  return explore(G, s, visit_func=visit_func)

def bfs(G, s, visit_func=lambda v: None):
  from collections import deque
  return explore(G, s, fringe_type=deque, pop_func=deque.popleft,
          visit_func=visit_func)

class PriorityQueue:
  """ Wrapper around heapq """
  import heapq
  def __init__(self):
    self.heap = []

  def __len__(self):
    return len(self.heap)

  def append(self, item):
    heapq.heappush(self.heap, item)

  def pop(self):
    return heapq.heappop(self.heap)

def ucs(G, s, visit_func=lambda v: None, return_distances=False):
  distances = dict.fromkeys(G.vertices.keys(), float("Inf"))
  distances[s] = 0
  def dist(dist, u, w):
    distances[u] = dist
    return dist+w
  res = explore(G, s, fringe_type=PriorityQueue,
                 pop_func=PriorityQueue.pop, distance_func=dist,
                 visit_func=visit_func)
  return res, distances if return_distances else res

def dijkstra(G, s, t):
  return ucs(G, s, return_distances=True)[1][t]

def test():
  g = Graph()
  A = g.add_vertex('A')
  B = g.add_vertex('B')
  C = g.add_vertex('C')
  D = g.add_vertex('D')
  E = g.add_vertex('E')
  F = g.add_vertex('F')
  G = g.add_vertex('G')
  g.add_edge(A, B, 7)
  g.add_edge(B, G, 1)
  g.add_edge(B, C, 2)
  g.add_edge(A, D, 1)
  g.add_edge(B, D, 5)
  g.add_edge(D, F, 4)
  g.add_edge(C, E, 3)
  g.add_edge(F, E, 2)

