#!/bin/bash

""" 
Some notes: 
Make sure to activate Firedrake venv.
Adjust path to Firedrake folder and MSc repository if necessary. 
Flame graphs will be saved as svg files in MSc-Project.
""" 

# Set OMP_NUM_THREADS=1
export OMP_NUM_THREADS=1

# Checkout Melina97/before_changes branch
cd ~/firedrake/src/firedrake 
git checkout Melina97/before_changes
cd ~/firedrake/src/PyOP2
git checkout Melina97/before_changes

# Enter MSc-Project repo
cd ~/Desktop/MScProject/Code/MSc-Project

# Create a flame graph for Melina97/before_changes branch
python Timing_experiment.py -log_view :flamegraph_before_changes.txt:ascii_flamegraph
./flamegraph.pl --title="Flame Graph: before changes" --countname="microseconds" flamegraph_before_changes.txt > flamegraph_before_changes.svg

# Checkout Melina97/after_changes branch
cd ~/firedrake/src/firedrake
git checkout Melina97/after_changes
cd ~/firedrake/src/PyOP2
git checkout Melina97/after_changes

# Enter MSc-Project repo
cd ~/Desktop/MScProject/Code/MSc-Project

# Create a flame graph for Melina97/after_changes branch
python Timing_experiment.py -log_view :flamegraph_after_changes.txt:ascii_flamegraph
./flamegraph.pl --title="Flame Graph: after changes" --countname="microseconds" flamegraph_after_changes.txt > flamegraph_after_changes.svg
