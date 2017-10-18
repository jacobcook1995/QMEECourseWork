## Script to look at whether the temperature is correlated with year
# Load data from file
load("../Data/KeyWestAnnualMeanTemperature.RData")
## Print out sample of table
print("The tabulated data")
ls.str()
## Now plot the Data
png('../Results/TempvsYear.png')
plot(ats$Year,ats$Temp)
invisible(dev.off())
## Now start on correlation part
a <- cor(ats$Temp[1:99],ats$Temp[2:100])# find correlation between year and temp
## Now need to generate a random sample of years + temps
# first initialise i
i <- 0
n <- 0 # count of number of samples with greater correlation than intial case
while(i<10000){
	Temps <- sample(ats$Temp, 100, replace = TRUE, prob = NULL)
	b <- cor(Temps[1:99], Temps[2:100])
	if(b > a){
		n = n + 1
	}
	i = i + 1
}
frac = n/10000.
print(frac)
