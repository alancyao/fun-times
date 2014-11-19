from pprint import pprint

""" Naive search. For each point in the grid,
    compute the sum of manhattan distances to
    each person """
def naive_search(n, people, print_grid=False):
  grid = [[0 for _ in range(n)] for __ in range(n)]
  for i in range(n):
    for j in range(n):
      distance = 0
      for person in people:
        distance += manhattanDistance((i,j), person)
      grid[i][j] = distance
  if print_grid:
    print 'Showing people grid'
    pgrid = [[0 for _ in range(n)] for __ in range(n)]
    for p in people:
      pgrid[p[0]][p[1]] = 1
    pprint(pgrid)
    print 'Showing distance grid'
    pprint(grid)
  miny = [min(enumerate(x), key=lambda p:p[1]) for x in grid]
  gridmin = min(enumerate(miny), key=lambda p:p[1])
  return gridmin[0], gridmin[1][0]

def manhattanDistance(p1, p2):
  return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

""" Run some tests, and print out the resulting grid """
def main():
  people = [(1, 1), (2, 4), (4, 1), (0, 2), (0, 0), (4, 4)]
  min_location = naive_search(5, people, True)
  print 'The min location: {}'.format(min_location)

if __name__ == '__main__':
  main()
