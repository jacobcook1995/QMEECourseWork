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


model <- lm(data = MyDF, Predator.mass ~ Type.of.feeding.interaction:Predator.lifestage:Location)
df = as.data.frame(summary(model)$coef)
write.csv(df, file = "../Results/PP_Regression_Results_Location.csv",row.names=FALSE)
