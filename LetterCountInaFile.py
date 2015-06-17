#!/usr/bin/env python
import mincemeat
import sys

file = open(sys.argv[1],'r')
data = list(file)
file.close()

datasource = dict(enumerate(data))

def mapfn(k, v):
  for letter in v:
    letter=letter.lower()
    if letter!="\n":
      yield letter, 1

def reducefn(k, vs):
  result = sum(vs)
  return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

resultlist = []

tot=0
for k in results.keys():
  tot=tot+int(results[k])

for k in results.keys():
  booval=float(float(results[k]*100)/float(tot))
  booval='%.2f' % booval
  boovall=str(booval)+"%"
  resultlist.append((k,boovall,results[k]))

resultlist = sorted(resultlist, key=lambda a: a[2])

for result in resultlist:
  print result
~
~
