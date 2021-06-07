
from firedrake import *
from firedrake_adjoint import *
from DG_advection_equation_with_upwinding import DG_advection_timing

# Run function without annotating tape (context manager)
with stop_annotating():
    DG_advection_timing(40, 40, 600.0, options={"ksp_max_it": 100, "ksp_type": "cg"})

# Timing experiment
DG_advection_timing(40, 40, 600.0, print_times=True, options={"ksp_max_it": 100, "ksp_type": "cg"})
