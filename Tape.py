
from firedrake import *
from firedrake_adjoint import *
from DG_advection_equation_with_upwinding import DG_advection_solve

DG_advection_solve(x_coords = 40, y_coords = 40, time_steps = 5.0, options={"ksp_max_it": 100, "ksp_type": "cg"})

tape = get_working_tape()
tape.visualise(output='tape_x.dot', launch_tensorboard=False, open_in_browser=True)
