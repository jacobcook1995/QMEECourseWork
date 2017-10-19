## Load Data in
MyDF <- read.csv("../Data/EcolArchives-E089-51-D1.csv")
## Load lattice module
library(lattice)
## Create pdf for Predator mass
pdf("../Results/Pred_Lattice.pdf", 11.7, 8.3)
h = densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data=MyDF)
print(h)
invisible(dev.off())
## Create pdf of Prey mass
pdf("../Results/Prey_Lattice.pdf", 11.7, 8.3)
f = densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data=MyDF)
print(f)
invisible(dev.off())
## Create pdf of Predator-Prey Size Ratio
pdf("../Results/SizeRatio_Lattice.pdf", 11.7, 8.3)
f = densityplot(~log(Predator.mass/Prey.mass) | Type.of.feeding.interaction, data=MyDF)
print(f)
invisible(dev.off())
## make 7 vectors
Types <- character(5)
Predator_median <- numeric(5)
Predator_mean <- numeric(5)
Prey_median <- numeric(5)
Prey_mean <- numeric(5)
Size_Ratio_median <- numeric(5)
Size_Ratio_mean <- numeric(5)
## Now move onto calculating mean and median of the data
# cycle feeding types
i <- 0
for (type in unique(MyDF$Type.of.feeding.interaction)){
	i = i + 1
	type_data <- subset(MyDF, Type.of.feeding.interaction == type)
	## calculate means and medians
	pred_med <- median(type_data$Predator.mass)
	pred_mean <- mean(type_data$Predator.mass)
	prey_med <- median(type_data$Prey.mass)
	prey_mean <- mean(type_data$Prey.mass)
	SR_med <- median(type_data$Prey.mass/type_data$Predator.mass)
	SR_mean <- mean(type_data$Prey.mass/type_data$Predator.mass)
	Types[i] <- type
	Predator_median[i] <- pred_med
	Predator_mean[i] <- pred_mean
	Prey_median[i] <- prey_med
	Prey_mean[i] <- prey_mean
	Size_Ratio_median[i] <- SR_med
	Size_Ratio_mean[i] <- SR_mean
}
# make a data frame using my vectors
df = data.frame(Types, Predator_median, Predator_mean, Prey_median, Prey_mean, Size_Ratio_median, Size_Ratio_mean)
# Now write as a csv without row numbering
write.csv(df, file = "../Results/PP_Results.csv",row.names=FALSE)
