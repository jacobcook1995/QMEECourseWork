#!/usr/bin/Rscript
# This function calculates heights of trees from the angle of
# elevation and the distance from the base using the trigonometric
# formula height = distance * tan(radians)
# ARGUMENTS:
# degrees
# distance
# The angle of elevation
# The distance from base
# OUTPUT:
# The height of the tree, same units as "distance"

TreeHeight <- function(degrees, distance){
	radians <- degrees * pi / 180
	height <- distance * tan(radians)	
	return (height)
}

filename <- commandArgs(trailingOnly = TRUE)

# Read the data from the file
filepath <- paste("../Data/", filename, sep = "") # add file path to file name
MyData <- read.csv(filepath, header = TRUE) # import with headers

# Then find tree height for each line and save as a list
Height.m <- TreeHeight(MyData[,3],MyData[,2])
# Make New Data frame
NewData <- data.frame(MyData, Height.m)

# Now write to new csv
filenamestrip = gsub("\\..*","",filename)
fileoutpath <- paste("../Results/", filenamestrip, "_treeheights.csv", sep = "")
write.csv(NewData, fileoutpath, row.names = FALSE) # ignore row names
