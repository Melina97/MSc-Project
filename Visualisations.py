
from firedrake import *
from firedrake_adjoint import *


# Create AdjFloats
a = AdjFloat(2)
b = AdjFloat(27)
c = AdjFloat(0.001)
d = AdjFloat(3.14)
e = AdjFloat(70)

# Perform operations
j = b*e
k = e**(1/a)
l = c+d
m = l-k
n = e/j
o = m-n

# Visualise the tape
tape = get_working_tape()
tape.visualise(output='tape_adjfloats.dot', launch_tensorboard=False, open_in_browser=True)
