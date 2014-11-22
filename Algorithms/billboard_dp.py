#!/usr/bin/python3

""" Problem description:
You have purchased a billboard. n advertisers come to you to rent the billboard. Each advertiser wants to pay you p_i dollars in order to rent the billboard from day s_i to day t_i, but the billboard can only display one ad at a time. Calculate the maximum amount of money you can make.
"""

""" Some variables for testing """
p = [6,23,56,18,6,3,4]
s = [0, 4, 3, 5,7,5,3]
t = [4, 6, 5, 8,8,6,5]

def find_max_profit(p,s,t):
  maximum = lambda x: max(x) if x else 0
  c = [0]*(max(t)+2)
  for i in range(len(c)-2,-1,-1):
    c[i] = max(c[i+1],
        maximum([p[adv_i]+c[t[adv_i]] for adv_i,j in enumerate(s) if j==i]))
  return c[0]

def main():
  print(p, s, t)
  print("Max profit: ", find_max_profit(p,s,t))

if __name__ == '__main__':
  main()
