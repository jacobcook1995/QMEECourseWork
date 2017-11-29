#!/usr/bin/env Rscript
# Script to implement neutral theory in R

# Clear up old data
rm(list=ls())
graphics.off()

# function that finds the number of unique elements in a community
species_richness <- function(community){
	ucommunity = unique(community, incomparables = FALSE)
	count = length(ucommunity)
	
	return (count) # this is optional but very useful
}

# function that generates a maximally diverse initial state of the simulation
initialise_max <- function(size){
	community = seq(from = 1, to = size, length.out = size)
	return (community) # return list
}

# function that generates a minimally diverse initial state of the simulation
initialise_min <- function(size){
	community = seq(from = 1, to = 1, length.out = size)
	return (community) # return list
}

# function that choose two non-repeating random integers between 1 and x
choose_two <- function(x){
	list = initialise_max(x) # use previous function
	pair = sample(list, 2, replace = FALSE) # sample without replacement
	
	return (pair) # return pair of values
}

# function to perform a single step of a simple neutral model simulation
neutral_step <- function(community){
	change = choose_two(length(community))
	new_community = replace(community, change[1], community[change[2]])
	return (new_community)
}

#function to perform several steps
neutral_generation <- function(community){
	N = length(community)/2
	# check if N is whole
	if (N%%1==0) {
		# Do nothing in this case
	} else {
		N = N + 0.5 # Otherwise make whole
	}
	# for loop to carry out multiple simulation steps
	for (i in 1:N){
		community = neutral_step(community)
	}
	return(community) # return new community
}

# function to perform neutral theory simulation and return a time series
neutral_time_series <- function(initial,duration){
	l = length(initial)
	time_series <- array(0,dim=c(duration + 1,l))
	time_series[1,1:l] = initial
	# iterate using my prior function
	for (i in 1:duration){
		time_series[i+1,1:l] = neutral_generation(time_series[i,1:l])
	}
	diversity_time_series = cbind(numeric(duration+1))
	for (i in 1:(duration+1)){
		diversity_time_series[i] = species_richness(time_series[i,1:l])
	}
	# now return this prior function
	return(diversity_time_series)
}

# function to plot graph 
question_8 <- function(){
	# Run for 100 individuals for 200 generations
    neutral_time_series = neutral_time_series(initialise_max(100), 200)
    jpeg('../Results/diversityplot.jpg')
    x <- plot(1:201,neutral_time_series, ann = FALSE)
    title(xlab="Time", col.lab=rgb(0,0.5,0))
    title(ylab="Species Diversity", col.lab=rgb(0,0.5,0))
    title(main="Species Diversity with Time", col.main="red", font.main=4)
    dev.off()
    return(0) # shouldn't return anything as this function is about plotting the graph
}

# Call function and plot graph
c = question_8()

# function to perform a step of the neutral model with speciation
neutral_step_speciation <- function(community,v){
	rand = runif(1)
	# test if rand is less than v
	if (rand <= v){ # if so then new species is added
		# need to find a species that isn't included already
		i = 0
		not_member = FALSE
		while (not_member == FALSE){
			i = i + 1
			if (i %in% community == FALSE){
				not_member = TRUE
				}
			}
		# Now have a value to replace with
		list = initialise_max(length(community)) # use previous function
	    index = sample(list, 1) # sample without replacement
	    community[index] = i
	} else {
		# otherwise conventional step is used
		community = neutral_step(community)
	}
	
	return(community)
}

# function to perform a generation level sample with speciation
neutral_generation_speciation <- function(community,v){
	N = length(community)/2
	# check if N is whole
	if (N%%1==0) {
		# Do nothing in this case
	} else {
		N = N + 0.5 # Otherwise make whole
	}
	# for loop to carry out multiple simulation steps
	for (i in 1:N){
		community = neutral_step_speciation(community,v)
	}
	return(community) # return new community
}

# function to simulate a certain number of generations with speciation
neutral_time_series_speciation <- function(initial,v,duration){
	l = length(initial)
	time_series <- array(0,dim=c(duration + 1,l))
	time_series[1,1:l] = initial
	# iterate using my prior function
	for (i in 1:duration){
		time_series[i+1,1:l] = neutral_generation_speciation(time_series[i,1:l],v)
	}
	diversity_time_series = cbind(numeric(duration+1))
	for (i in 1:(duration+1)){
		diversity_time_series[i] = species_richness(time_series[i,1:l])
	}
	# now return this prior function
	return(diversity_time_series)
}

# function to plot time series for speciation
question_12 <- function(){
	# Run for 100 individuals for 200 generations
    neutral_time_series = neutral_time_series_speciation(initialise_max(100),0.1, 200)
    jpeg('../Results/diversityplotspeciation.jpg')
    x <- plot(1:201,neutral_time_series,ann = FALSE)
    title(xlab="Time", col.lab=rgb(0,0.5,0))
    title(ylab="Species Diversity", col.lab=rgb(0,0.5,0))
    title(main="Species Diversity with Time", col.main="red", font.main=4)
    dev.off()
	return(0)
}
# call function 
d = question_12()

# function to find species abundances
species_abundance <- function(community){
	l = species_richness(community)
	abundances = cbind(numeric(l))
	alter_community = community
    for (i in 1:l){
		# find first element of community
		element = alter_community[1]
		# count the number of elements in the vector
		abundances[i] = sum(alter_community == element)
		# remove from the vector
		alter_community = alter_community[!alter_community == element]
	}
	abundances = sort(abundances, decreasing = TRUE)
	return(abundances)
}

# function to bin the species abundances into octaves
octaves <- function(abundances){
	
	return(octs)
}
octaves(c(100,64,63,5,4,3,2,2,1,1,1,1))
