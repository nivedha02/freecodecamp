import numpy as np

def calculate(list):

  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")

  a=np.array(list)
  b=a.reshape((3,3))

  mean=[np.mean(b,axis=0).tolist(),np.mean(b,axis=1).tolist(),np.mean(a)]
  variance=[np.var(b,axis=0).tolist(),np.var(b,axis=1).tolist(),np.var(a)]
  sd=[np.std(b,axis=0).tolist(),np.std(b,axis=1).tolist(),np.std(a)]
  ma=[np.max(b,axis=0).tolist(),np.max(b,axis=1).tolist(),np.max(a)]
  mea=[np.min(b,axis=0).tolist(),np.min(b,axis=1).tolist(),np.min(a)]
  s=[np.sum(b,axis=0).tolist(),np.sum(b,axis=1).tolist(),np.sum(a)]
  return{"mean":mean,
'variance':variance,
'standard deviation':sd,
'max':ma,
'min':mea,
'sum':s}

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
