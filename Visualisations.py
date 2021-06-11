
from firedrake import *
from firedrake_adjoint import *

# create AdjFloat

a = AdjFloat(2)
b = AdjFloat(3)
c = AdjFloat(27)
d = AdjFloat(3.14)
e = AdjFloat(999)
f = AdjFloat(0.001)
g = AdjFloat(7.54)
h = AdjFloat(70)

#operations

i = a+b
j = c*h
k = j/h
l = e/d
m = f-g
n = i**(a/l)
o = m-k
p = h/j
q = (n+p)**o

tape = get_working_tape()
tape.visualise(output='test1.dot', launch_tensorboard=False, open_in_browser=True)

