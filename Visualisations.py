
from firedrake import *
from firedrake_adjoint import *

# create AdjFloat

a = AdjFloat(2)
b = AdjFloat(27)
e = AdjFloat(0.001)
f = AdjFloat(3.14)
g = AdjFloat(70)

#operations

j = b*g
k = g**(1/a)
m = e+f
o = m-k
p = g/j
q = o-p

tape = get_working_tape()
tape.visualise(output='test1.dot', launch_tensorboard=False, open_in_browser=True)

