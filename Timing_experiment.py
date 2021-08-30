
from firedrake import *
from firedrake_adjoint import *
from DG_advection_equation_with_upwinding import DG_advection_solve, DG_advection_timing


# Run function without annotating tape (Cache warmup)
with PETSc.Log.Stage("Cache warmup"):
    with PETSc.Log.Event("Cache warmup"):
        DG_advection_solve(x_coords = 40, y_coords = 40, time_steps = 600.0, options={"ksp_max_it": 100, "ksp_type": "cg"})

# clear the tape before Timing run
tape = get_working_tape()
tape.clear_tape()

# Timing experiment
with PETSc.Log.Stage("Timing run"):
    with PETSc.Log.Event("Timing run"):
        DG_advection_timing(x_coords = 40, y_coords = 40, time_steps = 600.0, print_times=True, options={"ksp_max_it": 100, "ksp_type": "cg"})
