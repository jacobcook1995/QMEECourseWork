#!/bin/bash
# Author: Jacob Cook jc2017@imperial.ac.uk
# Script: run_get_TreeHeight.sh
# Desc: shell script to run the Vectorize R scripts and Python scripts
# Arguments: none
# Date: Oct 2017

echo ""
echo "Vectorize1.R times"
time Rscript Vectorize1.R >/dev/null
echo ""
echo "Vectorize1.py times"
time python Vectorize1.py
echo ""
echo "Vectorize2.R times"
time Rscript Vectorize2.R >/dev/null
echo ""
echo "Vectorize2.py times"
time python Vectorize2.py

#exit
