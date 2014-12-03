#!/usr/bin/env python3

""" Problem description:
You have a list of n people, each of whom has a first and a last name. You know that each person will use either their first or last name as a username, and then the list of usernames will be sorted. You are also given a permutation a_1, a_2, ..., a_n of the integers 1 through n. Provide an algorithm to determine whether it is possible that, after each person picks their username and the usernames are sorted, the 1st person in the original list will be in the a_1th position, the
2nd will be in the a_2th position, etc.
"""

""" Some variables for testing """
names = ['Bob Jones', 'Alan Yao', 'Joseph Hui', 'Lewin Gan',
    'Jason Khoe', 'Riyaz Firezullaboy', 'Edwin Xie']
a = [1, 0, 2, 4, 3, 5, 6]
a_impossible = [0, 1, 2, 4, 3, 5, 6]

def find_username_permutation(names, a):
  """ First arrange the names by the given permutation.
  Then greedily try to pick an ordering that will achieve
  the given permutation.
  If no ordering is possible, return None.
  """
  permuted = [names[i].split() for i in a]
  sorted_names = [min(permuted[0])]
  for firstname, lastname in permuted[1:]:
    if firstname > sorted_names[-1] and lastname > sorted_names[-1]:
      sorted_names.append(min(firstname,lastname))
    elif firstname > sorted_names[-1]:
      sorted_names.append(firstname)
    elif lastname > sorted_names[-1]:
      sorted_names.append(lastname)
    else:
      return None
  return sorted_names

def main():
  print("Names: {}\n, permutation: {}".format(names, a))
  print(find_username_permutation(names, a))
  print("Impossible permutation: {}".format([names[i] for i in a_impossible]))
  print("Impossible." if find_username_permutation(names, a_impossible) is None else "Failed to detect impossible permutation.")

if __name__ == '__main__':
  main()
