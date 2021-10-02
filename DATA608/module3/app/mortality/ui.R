library(shiny)

navbarPage( 
    title = div(
        div(
            style="padding: 0px 25x;",
            id = "img-id",
            img(src = "https://sps.cuny.edu/sites/all/themes/cuny/assets/img/header_logo.png", height="45%", width="45%", align="left")
        ),
        div(
            style="text-align: right;",
            "U.S Mortality"
        )
    ), 
    
    # Tab for Question 1: Neoplasm condition for 2010 is selected by default
    tabPanel("Question 1", inputId = 'q1Tab',
             
             sidebarLayout(
                 sidebarPanel(
                     
                     selectInput('mapCondition2',
                                 'Condition',
                                 Condition,
                                 selected = 'Neoplasms'),
                     
                     selectInput(inputId = 'mapYear2',
                                 label = h4('Year'),
                                 choices = Year,
                                 selected = 2010)
                 ),
                 
                 
                 mainPanel(
                     
                     HTML("<br>"),
                     p("Problem: As a researcher, you frequently compare mortality rates from particular causes across different States. You need a visualization that will let you see (for 2010 only) the crude mortality rate, across all States, from one cause (for example, Neoplasms, which are effectively cancers). Create a visualization that allows you to rank States by crude mortality for each cause of death."),
                     HTML("<br>"),
                     plotlyOutput("distPlot", height=600)
                 )
                 
                 

             )
    ),
    
    
    # Tab for Question 2: NY is selected as the default state
    tabPanel("Question 2", inputId = 'q2Tab',
             sidebarLayout(
                 sidebarPanel(
                     selectInput('mapState3',
                                 'State',
                                 State,
                                 selected = 'NJ'),
                     selectInput('mapCondition3',
                                 'Condition',
                                 Condition,
                                 selected = 'Diseases of the skin and subcutaneous tissue')
                     
                 ),
                 
                 
                 mainPanel(
                     HTML("<br>"),
                     p("Problem: Often you are asked whether particular States are improving their mortality rates (per cause) faster than, or slower than, the national average. Create a visualization that lets your clients see this for themselves for one cause of death at the time. Keep in mind that the national average should be weighted by the national population."),
                     HTML("<br>"),
                     plotlyOutput("statePlot", height=600)
                     )
                 
                 
                 
             )
    ),
    
    tabPanel("About", inputId = 'aboutTab',
                 mainPanel(
                     h1("Data 608 Fall 2021"),
                     h2("Author: Sung Lee"),
                     p("This Shiny App is for my class assignment. Additional resources are here:"),
                     HTML("<ul><li><a href='https://logicalschema.shinyapps.io/sung_lee_data608_hw3/'>Shiny App</a></li><li><a href='https://github.com/logicalschema/Fall-2021/tree/main/DATA608/module3'>GitHub for this App</a></li><li><a href='https://www.cdc.gov/cancer/uscs/about/hints.htm'>CDC Description for Dataset</a></li><li><a href='https://wonder.cdc.gov/wonder/help/ucd.html'>Additional CDC information</a></li><li><a href='https://github.com/charleyferrari/CUNY_DATA_608/tree/master/module3/'>Instructor&apos;s GitHub for this assignment</a></ul>")
                 )

    )

)