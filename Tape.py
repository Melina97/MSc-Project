
from firedrake import *
from firedrake_adjoint import *
from DG_advection_equation_with_upwinding import DG_advection_solve

DG_advection_solve(40, 40, 5.0, options={"ksp_max_it": 100, "ksp_type": "cg"})

tape = get_working_tape()
tape.visualise(output='tape.dot', launch_tensorboard=True, open_in_browser=False)
