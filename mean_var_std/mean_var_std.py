
import numpy as np

def calculate(l):
  a=np.array(l).reshape((3,3))
  b=np.array(l)
  d={}
  d['mean']= [(a.mean(axis=0)).tolist(), (a.mean(axis=1)).tolist(), b.mean()],
  d['variance']= [(a.var(axis=0)).tolist(),( a.var(axis=1)).tolist(), b.var()],
  d['standard deviation']= [(a.std(axis=0)).tolist(),(a.std(axis=1)).tolist(),b.std()],
  d['max']= [(a.max(axis=0)).tolist(), (a.max(axis=1)).tolist(),b.max()],
  d['min']= [(a.min(axis=0)).tolist(), (a.min(axis=1)).tolist(), b.min()],
  d['sum']= [(a.sum(axis=0)).tolist(), (a.sum(axis=1)).tolist(), b.sum()]

  return d

l=[0,1,2,3,4,5,6,7,8]
calculate(l)

