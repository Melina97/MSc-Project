
from firedrake import *
from firedrake_adjoint import *
from DG_advection_equation_with_upwinding import DG_advection_solve, DG_advection_timing

# Run function without annotating tape (context manager)
with PETSc.Log.Stage("Cache warmup"):
    with PETSc.Log.Event("Cache warmup"):
        DG_advection_solve(x_coords = 40, y_coords = 40, time_steps = 10.0, options={"ksp_max_it": 100, "ksp_type": "cg"})

tape = get_working_tape()
tape.clear_tape()

# Timing experiment
with PETSc.Log.Stage("Timing run"):
    with PETSc.Log.Event("Timing run"):
        DG_advection_timing(x_coords = 40, y_coords = 40, time_steps = 10.0, print_times=True, options={"ksp_max_it": 100, "ksp_type": "cg"})

"""
Last Run 10th June 12:46:
The taping takes: 10.799703121185303 seconds
Running the tape takes: 67.61313724517822 seconds
Computing the derivative of the reduced functional takes: 138.66187810897827 seconds
"""