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

## Create pdf to write plot to
pdf("../Results/PP_Regress_Plots.pdf", 11.7, 8.3)
p <- ggplot(MyDF, aes(x = Prey.mass, y = Predator.mass, colour = Predator.lifestage)) 
p <- p + geom_point(shape=3) + facet_grid(Type.of.feeding.interaction ~ .)
p <- p + theme(legend.position="bottom", aspect.ratio = 1/2)
p <- p + xlab("Prey mass in grams") + ylab("Predator mass in grams")
p <- p + scale_x_log10() + scale_y_log10()
p <- p + guides(colour=guide_legend(nrow=1))
p <- p + geom_smooth(method = "lm", fullrange = TRUE, size = 0.5)
suppressWarnings(print(p))
invisible(dev.off())

model <- lm(data = MyDF, Predator.mass ~ Type.of.feeding.interaction:Predator.lifestage)
df = as.data.frame(summary(model)$coef)
write.csv(df, file = "../Results/PP_Regression_Results.csv",row.names=FALSE)
