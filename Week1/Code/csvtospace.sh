#!/bin/bash
# Author: Jacob Cook jc2017@imperial.ac.uk
# Script: csvtospace.sh
# Desc: substitute the commas in the files with spaces
#        saves the output into a .csv file
# Arguments: 1-> tab delimited file
# Date: Oct 2017

echo "Creating a space delimited version of $1 ..."

cat $1 | tr -s "," " " >> $1.csv

echo "Done!"

exit
