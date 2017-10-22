################################################################
################## Wrangling the Pound Hill Dataset ############
################################################################
## This time done using tidyr instead of reshape 2
require(tidyr)
require(dplyr)

############# Load the dataset ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F)) 

# header = true because we do have metadata headers
MyMetaData <- read.csv("../Data/PoundHillMetaData.csv",header = T, sep=";", stringsAsFactors = F)

############# Inspect the dataset ###############
dplyr::tbl_df(MyData)
dim(MyData)
dplyr::glimpse(MyData)
utils::View(MyData) #you can also do this
utils::View(MyMetaData)

############# Transpose ###############
# To get those species into columns and treatments into rows
MyData <- t(MyData) 
dplyr::tbl_df(MyData)
dim(MyData) 

############# Replace species absences with zeros ###############
MyData[MyData == ""] = 0

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!
colnames(TempData) <- MyData[1,] # assign column names from original data

############# Convert from wide to long format  ###############
require(reshape2) # load the reshape2 package
dplyr::tbl_df(TempData)
utils::View(TempData)
dim(TempData)
MyWrangledData <- tidyr::gather(TempData, Species, Count, -Cultivation, -Block, -Plot, -Quadrat)

dplyr::glimpse(MyWrangledData)
dplyr::tbl_df(MyWrangledData)
dim(MyWrangledData)

############# Start exploring the data (extend the script below)!  ###############
