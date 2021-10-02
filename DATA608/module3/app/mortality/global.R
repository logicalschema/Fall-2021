#https://shiny.rstudio.com/gallery/superzip-example.html

library(leaflet)
library(leaflet.extras) #for demo heat map
library(geojsonio)

library(maps)
library(ggplot2)
library(dplyr)
library(lubridate)
library(tidyr)
library(forcats)
library(plotly)
library(scales)
library(stringr)




# "ICD.Chapter" "State"       "Year"        "Deaths"      "Population"  "Crude.Rate"
# Additional information about the dataset is here: https://wonder.cdc.gov/wonder/help/ucd.html and https://www.cdc.gov/cancer/uscs/about/hints.htm
# Reading the cleaned-cdc-mortality-1999-2010-2.csv file
data <- read.csv("cleaned-cdc-mortality-1999-2010-2.csv", 
                 sep = ",", 
                 header = TRUE)




# variables
Year <- c(min(data$Year):max(data$Year))
State <- sort(unique(data$State))
Condition <- sort(unique(data$ICD.Chapter))


# Leaflet
# https://eric.clst.org/tech/usgeojson/
# https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_500k.json

# "GEO_ID"     "STATE"      "NAME"       "SHORTNAME"  "CENSUSAREA"
states <- geojson_read("us_states.json", what = "sp")










