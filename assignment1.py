import numpy
import math

n=100
y_hat=np.rando.rand(n)
y=np.rando.randint(0,2,n)

o=0
for i in range(0,n):
  o=-(y[i]*math.log2(y_hat[i]) + (1-y[i])*math.log2(1-y_hat[i]))
o=o/n
print('The value of the cross entropy function ',o)
