import sys
lines = sys.stdin.readlines()
if sorted(lines[0]) == sorted(lines[1]):
  print "Anagrams!"
else:
  print "Not anagrams!"
