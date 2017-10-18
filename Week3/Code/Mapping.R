## Script to make maps of data
# loads maps package
library(maps)
# Load data from file
load("../Data/GPDDFiltered.RData")

## get world map data, and make into a map
png('../Results/WorldMap.png')
map('world', fill = TRUE, col = 1:20)
invisible(dev.off())
## Now merge world map with the data I've been provided with and loaded
png('../Results/OurMap.png')
map('world')
points(gpdd$lon, gpdd$lat, col = "red", cex = .6)
invisible(dev.off())

## The vast majority of this data seems to have been collected in the "First World"
## across a range of longitudes and latitudes. This suggests a lot of the distribution
## of data is likely to be due to the ability/desire of goverments to collect this sort
## of data rather than anything particularly profound
