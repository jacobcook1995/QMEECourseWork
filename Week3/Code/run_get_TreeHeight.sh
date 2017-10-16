#!/bin/bash
# Author: Jacob Cook jc2017@imperial.ac.uk
# Script: run_get_TreeHeight.sh
# Desc: shell script to run the get_TreeHeight.R R script
# Arguments: none
# Date: Oct 2017

Rscript get_TreeHeight.R trees.csv
ipython get_TreeHeight.py trees2.csv

#exit
