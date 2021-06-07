
from firedrake import *
from firedrake_adjoint import *
from DG_advection_equation_with_upwinding import DG_advection_timing
import math
import time

# Run the function without annotating the tape
with stop_annotating():  # context manager
    DG_advection_timing(40, 40, 600.0, options={"ksp_max_it": 100, "ksp_type": "cg"})

# Timing experiment
DG_advection_timing(40, 40, 600.0, print_times=True, options={"ksp_max_it": 100, "ksp_type": "cg"})
