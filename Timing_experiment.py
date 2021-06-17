
from firedrake import *
from firedrake_adjoint import *
from DG_advection_equation_with_upwinding import DG_advection_timing

# Run function without annotating tape (context manager)
with stop_annotating():
    DG_advection_timing(x_coords = 40, y_coords = 40, time_steps = 600.0, options={"ksp_max_it": 100, "ksp_type": "cg"})

# Timing experiment
DG_advection_timing(x_coords = 40, y_coords = 40, time_steps = 600.0, print_times=True, options={"ksp_max_it": 100, "ksp_type": "cg"})


"""
Last Run 10th June 12:46:
The taping takes: 10.799703121185303 seconds
Running the tape takes: 67.61313724517822 seconds
Computing the derivative of the reduced functional takes: 138.66187810897827 seconds
"""