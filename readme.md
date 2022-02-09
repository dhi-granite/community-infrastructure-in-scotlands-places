# Scottish Communities

## Introduction

This dashboard is part of a project run by the David Hume Institute, in partnership with the William Grant Foundation, with the assistance of many other organisations and individuals across Scotland. The project aims to analyse open data about Scotland’s places in order to better understand how community assets and community infrastructure (such as community meeting spaces, businesses, local charities, mutual aid organisations, and development trusts) benefit the communities that they are located in. These types of assets are often left out of analyses of infrastructural inequalities, but they can provide crucial support to communities.

Our key questions of interest were:

- A general question about community assets in Scotland


- Is there a relationship between the number of businesses per capita and the number of charities per capita in an intermediate zone?
- If so, what is the nature of this relationship?
- Is there a relationship between the number of businesses per capita and the number of community spaces per capita in an intermedate zone?
- If so, what is the nature of this relationship?
- Is there a relationship between the number of charities per capita and the number of community spaces per capita in an intermediate zone? 
- If so, what is the nature of this relationship?
- How does the SIMD relate to these three types of community assets?

The dashboard allows us to look at the relationship between Scottish Index of Multiple Deprivation (SIMD) rankings and these community assets/infrastructure on a map as well as in various graphs. The project uses intermediate zones as the boundaries of communities – while this is not always an accurate representation of where community boundaries lie, it is the most granular scale available for a lot of open data.


The main findings are that across Scotland
 
- There seems to be a positive relationship between the number of businesses per capita and the number of charities per capita in an intermediate zone.
 
- There seems to be a positive relationship between the number of charities per capita and community spaces per capita in an intermediate zone.
 
- There seem to be less charities in communities defined as more deprived by the SIMD.
 
- There seem to be less businesses in communities defined as most deprived and least deprived by the SIMD.
 
- There seem to be more community spaces in communities defined as more deprived by the SIMD.

## Dashboard

In the dashboard, there is one main page with a summary table. Then there is a separate page for each local authority. Each local authority page has seven tabs.

### The main page

This is a screenshot of the summary table. The data comes from the data/scotland/la_info.csv file. 

![A screenshot of the summary table, with a row for each local authority. The columns are 'Local authority', 'Mean SIMD decile', 'Businesses per 1000 people', 'Charities per 1000 people', 'Community spaces per 1000 people', 'Mutual aid organisations per 100,000 people' and 'Development trusts per 100,000 people'.](/assets/images/summary_table.png)

### Local authority pages

#### Mutual aid organisation and the Scottish Household Survey
At the top of each local authority page, I have included some figures for the whole local authority. These are the number of mutual aid organisations per 100,000 people, and the percentage of people in the local authority who say that they could rely on someone in their neighbourhood to help them (this percentage comes from the Scottish Household Survey). 

#### Tab 1
This tab contains a map of the local authority, with information about each intermediate zone that appears when you scroll over an intermediate zone on the map. There are also points plotted for community spaces, charities, development trusts, and mutual aid organisations. Below is the map for the City of Edinburgh, with charities selected, and the intermediate zone information for Balerno and Bonnington Village being displayed. The maps are stored in the assets folder.

![A screenshot of the first tab for the City of Edinburgh page. There is a map, with options to see the locations of community spaces, charities, development trusts, or mutual aid organisations. The intermediate zone of Balerno and Bonnington Village is highlighted, with information on the intermediate zone displayed in a tooltip. The information is the name of the intermediate zone, the mean SIMD decile, female life expectancy, male life expectancy, businesses per 1000 people, and charities per 1000 people.](/assets/images/tab_1.png)

#### Tab 2
The second tab contains a table with a row of information for each intermediate zone in the local authority in alphabetical order. Each row has the columns ‘Community’ (Intermediate zone name), ‘Mean SIMD decile’ (the average of the datazone SIMD deciles that make up the intermediate zone), ‘Female life expectancy’, ‘Male life expectancy’, ‘Businesses per 1000 people’, ‘Local charities per 1000 people’, and ‘Community spaces per 1000 people’. I’ve included a screenshot of the top of the table for Inverclyde below. 

![A screenshot of the second tab for the Inverclyde page. There is a table with information on each intermediate zone displayed. The columns display the same information as in the tooltip on the map in tab 1.](/assets/images/tab_2.png)

#### Tab 3
The third tab shows the mean number of charities per 1000 people for each decile of the SIMD within the local authority in a bar plot. When you hover over one of the bars, you can see the SIMD decile, the mean number of charities per 1000 people, and the range (minimum and maximum) for the number of charities per 1000 people in intermediate zones of that decile within the local authority. Here you can see the mean number of charities per 1000 people in intermediate zones that fall into the fourth SIMD decile in the City of Edinburgh, as well as the range in numbers of charities per 1000 people in these intermediate zones.

![A screenshot of the third tab for the City of Edinburgh page. There is a bar plot, with the mean number of charities per 1000 people on the y axis and the SIMD decile of intermediate zones on the x axis. The third decile is highlighted, with a tooltip showing the decile, mean number of charities per 1000 people, and the range for values in that decile.](/assets/images/tab_3.png)

#### Tab 4
The fourth tab is similar to the third tab, but we are looking at the mean number of businesses per 1000 people in intermediate zones that fall into each decile within the selected local authority instead of the mean number of charities per 1000 people. 

![A screenshot of the fourth tab for the City of Edinburgh page. There is a bar plot showing the mean number of businesses per 1000 people in each decile of the SIMD for the City of Edinburgh.](/assets/images/tab_4.png)

#### Tab 5
The fifth tab shows the mean number of community spaces per 1000 people in intermediate zones of each decile of the SIMD. Below, you can see the bar plot for Glasgow City, with the figures for intermediate zones in the third decile of the SIMD highlighted. 

![A screenshot of the fifth tab for Glasgow City. There is a bar plot showing the mean number of community spaces per 1000 people in each decile of the SIMD in Glasgow City.](/assets/images/tab_5.png)

#### Tab 6
The sixth tab contains a scatter plot of the number of businesses per 1000 people and the number of charities per 1000 people in the selected local authority to show whether there is a relationship between these two variables. Each point on the graph represents an intermediate zone. Below I have included the scatterplot for Inverclyde, with the ‘Port Glasgow Upper, West and Central’ intermediate zone selected.

![A screenshot of the sixth tab for Inverclyde. There is a scatter plot showing the number of businesses per 1000 people against the number of charities per 1000 people in all intermediate zones in Inverclyde.](/assets/images/tab_6.png)

#### Tab 7
The seventh and final tab contains a scatter plot that shows the relationship between the number of charities per 1000 people and the number of community spaces per 1000 people in intermediate zones within a local authority. I’ve included a screenshot of the scatter plot for Clackmannanshire below, with the ‘Alloa South and East’ intermediate zone selected as an example.

![A screenshot of the seventh tab for Clackmannanshire. There is a scatter plot showing the number of charities per 1000 people against the number of community spaces per 1000 people in all intermediate zones in Clackmannanshire.](/assets/images/tab_7.png)

## Running Instructions

- Download the files necessary to run the dashboard on your computer.
    - If you are familiar with git and have it installed on your computer, you can clone the repository by clicking the ‘Code’ button and copying then running the command displayed there in your command line.
    - Otherwise, you can download a zip file of the project by clicking the ‘Code’ button, then selecting ‘Download ZIP’. 
- Install the dependencies. These are listed below, at the top of the Methods section.
- You should then be able to get the dashboard running locally by navigating to the running the following command in your command line:

```
python3 index.py
```

- The project runs by default on port 8050, at http://localhost:8050/


