# empty the workspace
rm(list=ls())

# close any open pdfs
if (length(dev.list())>0){
	dev.off()
}

# open lattice structure
library(ggplot2)
library(lattice)

# Read in my csv data
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")

par(mfcol=c(5,1)) #initialize multi-paneled plot
# PANEL1
par(mfg = c(1,1))
qplot(log(Prey.mass), log(Predator.mass), data = MyDF, geom = c("point", "smooth"))

# PANEL2
par(mfg = c(2,1))

# PANEL3
par(mfg = c(3,1))

# PANEL4
par(mfg = c(4,1))

# PANEL5
par(mfg = c(5,1))
