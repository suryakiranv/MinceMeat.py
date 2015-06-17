#!/usr/bin/env python
import mincemeat
import sys

data = []
combarr = []
temparr = []
temp = 0

def comb(length, possibles):
  ret = []
  if length == 1:
    return possibles
  else:
    subs = comb(length -1, possibles)
    for ch in possibles:
      for sub in subs:
        ret.append(str(ch) + str(sub))
  return ret

combarr = comb(4,"abcdefghijklmnopqrstuvwxyz0123456789")

for string in combarr:
    if temp!=4000:
      temparr.append(string)
      temp = temp + 1
    else:
     data.append(temparr)
     temp = 0
     temparr = []


hashedString = sys.argv[1]
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
  import hashlib
  for string in v:
    m = hashlib.md5()
    m.update(string)
    hashe = m.hexdigest()
    hashe = hashe[:5]
    yield hashe, string


def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
for key in results.keys():
  if(hashedString == key):
    print " "+str(hashedString)+" is :"+str(results[key])
