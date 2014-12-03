#!/usr/bin/env python3
""" Problem description:
You have a garden full of n apple trees. Each tree has a_i apples on it, which will ripen on day b_i. They can be harvested on day b_i and day b_i+1 (that is, for two days), after that the apples will rot. Each day you can harvest up to v apples. Calculate the maximum number of apples you can harvest.
"""

""" Some variables for testing """
a = [10, 5, 1, 2, 1, 1, 3, 7, 1, 1]
b = [0,  0, 1, 1, 2, 2, 3, 3, 4, 4]
v = 7

def find_max_harvest(a, b, v):
  """ Greedy solution. First notice that if two trees can be
  harvested on the same day, it is semantically the same as a single
  tree being harvested on that day, so we can merge all duplicates.
  Then we can scan through the days, picking a maximal amount of
  apples per day from the trees available in day i and i-1.
  """
  harvests = {}
  for day, amt in zip(b, a):
    if day in harvests:
      harvests[day] += amt
    else:
      harvests[day] = amt
  total = 0
  for i in range(max(list(harvests.keys()))+2):
    prev_picked, current_picked = 0, 0
    if i-1 in harvests:
      prev_picked = min(v, harvests[i-1])
    if i in harvests:
      current_picked = min(v-prev_picked, harvests[i])
      harvests[i] -= current_picked
    print("Picking {} on day {}".format(prev_picked+current_picked, i))
    total += (prev_picked + current_picked)
  return total

def main():
  print("a, b, v:", a, b, v, sep="\n")
  print("max: ", find_max_harvest(a, b, v))

if __name__ == '__main__':
  main()
