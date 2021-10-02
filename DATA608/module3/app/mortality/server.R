#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define server logic required to draw a histogram
shinyServer(function(input, output, session) {

    output$distPlot <- renderPlotly({
        withProgress(message = 'Calculations in progress',
                     detail = 'Loading...', value = 0, {
                         for (i in 1:10) {
                             incProgress(1/10)
                             Sys.sleep(0.01)
                         }
                    })
        yearselect <- input$mapYear2
        conditionselect <- input$mapCondition2
        
        
        temp <- data[data$Year == yearselect & data$ICD.Chapter == conditionselect,]
        
        temp <- temp %>% mutate(State = fct_reorder(State, Crude.Rate))
        
        
        p <- ggplot(data=temp, aes(x=State, y=Crude.Rate)) + 
            geom_bar(stat="identity", fill="firebrick2") +
            labs(title = paste("Crude Mortality Rate by State for ", conditionselect, ": ", yearselect, sep="")) + 
            xlab("State") +
            ylab("Crude Mortality Rate") +
            coord_flip() +
            theme(panel.grid.major = element_blank(), 
                  panel.grid.minor = element_blank(), 
                  panel.background = element_blank(), 
                  axis.line = element_line(colour = "black") 
            )
        
        p
        
        
    })
    
    
    output$statePlot <- renderPlotly({
        withProgress(message = 'Calculations in progress',
                     detail = 'Loading...', value = 0, {
                         for (i in 1:10) {
                             incProgress(1/10)
                             Sys.sleep(0.01)
                         }
                     })
        
        stateSelect <- input$mapState3
        conditionselect <- input$mapCondition3

        
        # Dataframe for the condition
        temp <- data[data$ICD.Chapter == conditionselect,]
        
        # To get the national average
        agg_sum <- aggregate(temp[,c("Deaths", "Population")],by=list(temp$Year),FUN=sum, na.rm=TRUE)
        agg_sum['NationalAverage'] <- agg_sum$Deaths / agg_sum$Population * 100000
        
        #Year, Deaths, Population, NationalAverage
        colnames(agg_sum)[1] <- "Year"
        
        tempState <- temp[temp$State == stateSelect,]
        tempState$NationalAverage <- agg_sum$NationalAverage[match(tempState$Year, agg_sum$Year)]
        
        
        plotState <- tempState %>% select(Year, Crude.Rate, NationalAverage) %>% gather("Category", "Value", -Year)
        
        q <- ggplot(data=plotState, aes(x = Year, y = Value, fill = Category)) +
            geom_col(position = "dodge") +
            labs(title = paste(stateSelect, ": Crude Mortality Rate for ", conditionselect, sep="")) +
            xlab('Year') +
            ylab('Rate') +
            scale_fill_manual(values = c("steelblue", "springgreen")) +
            scale_x_continuous(breaks= pretty_breaks()) +
            theme(panel.grid.major = element_blank(), 
              panel.grid.minor = element_blank(), 
              panel.background = element_blank(), 
              axis.line = element_line(colour = "black") 
            )
            
        
        q

        
        
    })
    
    
    output$usmap <- renderLeaflet({ 
        withProgress(message = 'Calculations in progress',
                     detail = 'Loading...', value = 0, {
                         for (i in 1:20) {
                             incProgress(1/10)
                             Sys.sleep(0.01)
                         }
                     })
        
        mapYearSelect <- input$mapYear
        mapConditionSelect <- input$mapCondition
        
        temp2 <- data[data$Year == mapYearSelect & data$ICD.Chapter == mapConditionSelect,]
        
        # Used for replacing NA values
        replaceValue <- mean(temp2$Crude.Rate, na.rm=TRUE)
        
        names(states)
        
        
        states$Crude.Rate <- temp2$Crude.Rate[match(states$SHORTNAME, temp2$State)]
        states$Crude.Rate[is.na(states$Crude.Rate)] <- replaceValue
        
        
        
        
        #bins <- c(0, 10, 20, 50, 100, 200, 500, 1000, Inf)
        #pal <- colorBin("YlOrRd", domain = states$Crude.Rate, bins = bins)
        
        x <- cut(temp2$Crude.Rate, 3, include.lowest=TRUE)
        z <- sapply(str_extract_all(x, "-?[0-9.]+"), function(y) max(as.numeric(y)))
        z <- unique(sort(z))
        z <- c(0, z, Inf)
        
        bins <- z
        pal <- colorBin("Reds", domain = states$Crude.Rate, bins = bins)
        
        labels <- sprintf(
            "<strong>%s</strong><br/>%g Crude.Rate",
            states$NAME, states$Crude.Rate
        ) %>% lapply(htmltools::HTML)
        
        
        leaflet(states) %>%
            setView(-96, 37.8, 4) %>%
            addProviderTiles("MapBox", options = providerTileOptions(
                id = "mapbox.light",
                accessToken = Sys.getenv('pk.eyJ1IjoiY3VueXNzbGVlIiwiYSI6ImNrdTlzNmF4azA5dzYyeG5ubXZvZDRxbzQifQ.Z4cygOgWVTTt9DkUVkCbgw'))) %>%
            addPolygons(
                fillColor = ~pal(Crude.Rate),
                weight = 2,
                opacity = 1,
                color = "white",
                dashArray = "3",
                fillOpacity = 0.7,
                highlightOptions = highlightOptions(
                    weight = 5,
                    color = "#666",
                    dashArray = "",
                    fillOpacity = 0.7,
                    bringToFront = TRUE),
                label = labels,
                labelOptions = labelOptions(
                    style = list("font-weight" = "normal", padding = "3px 8px"),
                    textsize = "15px",
                    direction = "auto")) %>%
            addLegend(pal = pal, values = ~density, opacity = 0.7, title = NULL,
                      position = "bottomright")

    })
        

})
