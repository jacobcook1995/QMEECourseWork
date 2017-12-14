#!/usr/bin/env Rscript
# Script to for a single cluster run for a given speciation rate, size, 
# wall time, interval richness, interval octaves, burn in generations
# also reads in an output file name

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
	# take log 2 of abundances
	labundances = log(abundances, base = 2)
	
	# cinvert data into an integer vector
	bin = floor(labundances) + 1 # +1 to ensure 1st element is 1 not 0
	# Now tabulate the data
	octs = tabulate(bin, nbins = max(1, bin, na.rm = TRUE))
	
	return(octs)
}

cluster_run <- function(speciation_rate,size,wall_time,interval_rich,interval_oct,burn_in_generations,output_file_name){
	# wall time is in minutes, speciation rate elsewhere refered to as v probabilty of speciation rather than replacement
	# burn in period is the number of generations to record species richness for
	# interval_rich gives how many genrations should occcur between recordings of the species richness,
	# interval_oct is equivalent but for the species abundance octaves
	PTM <- proc.time() # total simulation time clock started
	community = initialise_min(size)
	Time = 60*wall_time # convert wall_time into seconds
	wall_time_finished = FALSE
	# preallocate vector
	spec_rich <- vector(mode = "numeric", length = (burn_in_generations/interval_rich)+1)
	spec_rich[1] = species_richness(community)
	# make new list for octaves
	octs = list(octaves(species_abundance(community)))
	i = 0 # set generation number to 0
    # Start the clock!
    ptm <- proc.time()
    while (wall_time_finished == FALSE){
		community = neutral_generation_speciation(community,speciation_rate)
		i = i+1
		# if loop to decide if species richness should be stored
		if(i <= burn_in_generations && i%%interval_rich == 0){
			spec_rich[(i/interval_rich)+1] = species_richness(community)
		}
		# if loop to decide if species abundance octaves should be stored
		if(i%%interval_oct == 0){
			octs[[1+(i/interval_oct)]] <- octaves(species_abundance(community))
		}
		# Stop the clock
        time = proc.time()[3] - ptm[3]
        if (time > Time){
			wall_time_finished = TRUE # set true and end loop once time is elapsed
		}
	}
	TIME = proc.time()[3] - PTM[3] # Total simulation time found
	data = list(spec_rich,octs,community,TIME,speciation_rate,size,wall_time,interval_rich,interval_oct,burn_in_generations)
	# save data to file given by file name
	saveRDS(data, output_file_name)

	return() # returning NULL as it doesn't actually matter what is returned, this might be problematic with HPC though
}

# Get iteration number from system, commented out for now
iter <- as.numeric(Sys.getenv("PBS_ARRAY_INDEX"))
set.seed(iter) # seed random numbers
speciation = 0.005102 # my speciation rate
# determine population size J
if ((iter)%%4 == 1){
	J = 500
} else if ((iter)%%4 == 2){
	J = 1000
} else if ((iter)%%4 == 3){
	J = 2500
} else if ((iter)%%4 == 0){
	J = 5000
}
# use J to obtain octave intervals and burn times
int_oct = J/10
burn_t = 8*J
# Now use iter to make filename
filename = paste("my_test_file", iter, sep = "_")
outfilename = paste(filename, ".rda", sep = "")
# rich_int is 1 for all simulations
rich_int = 1
# convert time in hours to time in minutes
runtime = 11.5*60
cluster_run(speciation,J,runtime,rich_int,int_oct,burn_t,outfilename)
