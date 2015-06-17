#!/usr/bin/env python

import mincemeat
import sys

inp=sys.argv[1]
file = open(inp,'r')
data = list(file)
file.close()

datasource = dict(enumerate(data))

def mapfn(k, v):  
  yield 'Sol',int(v)  

def reducefn(k, vs):
  import math
  lisp=[]
  count=0
  summ=0
  for vi in vs:
    summ=summ+vi
    lisp.append(vi)
    count=count+1
  mean=summ/count
  sqsum=0
  for vii in lisp:
    sqsum=sqsum+((vii-mean)*(vii-mean))
  booval=sqsum/count
  count="Count: " + str(count) 
  stadev=math.sqrt(booval)
  stadev=float(stadev)
  stadevi="Std.dev: " + str(stadev) 
  result ="Sum: "+ str(sum(vs))
  return count,result,stadevi
 
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

res=[]
for element in results.keys():
  res.append(results[roo])

for element in res:
  print element
