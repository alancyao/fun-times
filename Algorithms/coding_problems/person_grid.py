from pprint import pprint

"""
You have a nxn grid of people.
Find the location (i, j) that minimizes the
manhattan distance to each person.
"""

def naive_search(n, people, print_grid=False):
  """ Naive search. For each point in the grid,
  compute the sum of manhattan distances to
  each person.
  """
  grid = [[0 for _ in range(n)] for __ in range(n)]
  for i in range(n):
    for j in range(n):
      distance = 0
      for person in people:
        distance += manhattanDistance((i,j), person)
      grid[i][j] = distance
  if print_grid:
    print 'Showing distance grid'
    pprint(grid)
  miny = [min(enumerate(x), key=lambda p:p[1]) for x in grid]
  gridmin = min(enumerate(miny), key=lambda p:p[1])
  return gridmin[0], gridmin[1][0]

def print_grid(n, people, sln=None):
  """ Print the grid for visualization """
  print 'Showing people grid'
  pgrid = [[0 for _ in range(n)] for __ in range(n)]
  for p in people:
    pgrid[p[0]][p[1]] = 1
  pprint(pgrid)
  if sln:
    print 'Showing solution location'
    sgrid = [[0 for _ in range(n)] for __ in range(n)]
    sgrid[sln[0]][sln[1]] = 1
    pprint(sgrid)

def search(n, people):
  """ Find the optimal location by median-finding """
  x_locs = sorted([i[0] for i in people])
  y_locs = sorted([i[1] for i in people])
  median = len(x_locs)/2
  return x_locs[median], y_locs[median]

def manhattanDistance(p1, p2):
  return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def main():
  """ Run some tests, and print out the resulting grid """
  n=5
  people = [(1, 1), (2, 4), (4, 1), (0, 2), (0, 0), (4, 4)]
  min_location = naive_search(5, people, True)
  print 'The min location: {}'.format(min_location)
  print_grid(n,people,min_location)
  min_location = search(5, people)
  print 'The min location: {}'.format(min_location)
  print_grid(n,people,min_location)

if __name__ == '__main__':
  main()
