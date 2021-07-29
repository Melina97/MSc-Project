#!/bin/bash

# set OMP_NUM_THREADS=1
export OMP_NUM_THREADS=1

# activate venv
# source firedrake/bin/activate

# checkout master branch
cd ~/firedrake/src/firedrake 
git checkout Melina97/before_changes
cd ~/firedrake/src/PyOP2
git checkout master
#git checkout Melina97/before_changes

# enter MSc repo
cd ~/Desktop/MScProject/Code/MSc-Project

# make flame graph for master branch
python Timing_experiment.py -log_view :flamegraph_without_changes.txt:ascii_flamegraph
./flamegraph.pl --title="Flame Graph: before changes" --countname="microseconds" flamegraph_without_changes.txt > flamegraph_without_changes.svg

# checkout Melina97/cache_assign branch and Melina97/fix_cache_problem branch
cd ~/firedrake/src/firedrake
git checkout Melina97/after_changes
cd ~/firedrake/src/PyOP2
git checkout master
#git checkout Melina97/after_changes

# enter MSc repo
cd ~/Desktop/MScProject/Code/MSc-Project

# make flame graph for Melina97/cache_assign branch
python Timing_experiment.py -log_view :flamegraph_with_changes.txt:ascii_flamegraph
./flamegraph.pl --title="Flame Graph: after changes" --countname="microseconds" flamegraph_with_changes.txt > flamegraph_with_changes.svg
