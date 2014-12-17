#!/usr/bin/env python
import csv
import os
import sys

#REGISTER_PATH = '/home/ff/cs170/grading/register/'
sid2login = {}
REGISTER_PATH = 'register/'

def populate_students():
  logins = os.listdir(REGISTER_PATH)
  for login in logins:
    with open(REGISTER_PATH + login, 'r') as f:
      for line in f:
        s = line.split()
        if s[0] == 'SID:':
          sid2login[s[1]] = login

def translate_CSV(fname):
  grades = {}
  with open(fname, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for subm in reader:
      grades[subm['SID']] = subm['Total Score']
  return grades

def write_glookup_file(grades, fname):
  with open(fname, 'w') as f:
    for sid, grade in grades.iteritems():
      if sid in sid2login:
        line = "{} - {}\n".format(sid2login[sid], grade)
        f.write(line)
      else:
        print "Unregistered student with SID: %s" % sid

def main():
  if len(sys.argv) < 2:
    print 'Provide a csv filename as input'
    return 0
  populate_students()
  grades = translate_CSV(sys.argv[1])
  write_glookup_file(grades, ''.join(sys.argv[1].split('_')[:-1]).lower())

if __name__ == '__main__':
  main()
