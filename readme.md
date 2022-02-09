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

This is a screenshot of the summary table. The data comes from the /data/scotland/la_info.csv file. 

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

## Version Information

#### Dependencies (necessary to run the dashboard)

| Dependency | Version |
| --- | --- |
| Python | 3.7.10 |
| Dash | 2.0.0 |
| Dash Bootstrap Components | 1.0.0 |

#### Other libraries used

| Library | Version |
| --- | --- |
| Pandas | 1.3.2 |
| Geopandas | 0.9.0 |
| Folium | 0.12.0 |
| Seaborn | 0.11.2 |
| BeautifulSoup4 | 4.10.0 |
| Jupyter | 1.0.0 |
| Plotly | 5.4.0 |
| Scipy | 1.7.1 |


## Methods

### Data at whole-Scotland level

#### Charity data
I downloaded the OSCR Charity Register from [here](https://www.oscr.org.uk/about-charities/search-the-register/charity-register-download/). I then filtered it to include only charities with a “Geographical Spread” of “A specific local point, community, or neighbourhood” or “Wider, but within one local authority area”. 

To remove charities where the “Main Operating Location” listed for the charity was not in the same local authority as the postcode of its head office, I used the Postcode Index from National Records of Scotland ([here](https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products/scottish-postcode-directory/2021-2)). Though some charities operating locally as well as in other areas will have been removed during this process, it was the best available approximation for local charities.
 
#### Mutual aid organisation data
For mutual aid organisations, I made a get request to [this](https://mutualaid.wiki/api/group/get) API endpoint, which returns a json string with all mutual aid organisations in the Mutual Aid Wiki database. This list of organisations contains global organisations, so I took only those with a “location_country” attribute of “GB” into a new list. 

The mutual aid organisation objects had coordinates but not always a full address, so I used the latitude and longitude extremes for Scotland to filter out most of the organisations not in Scotland, then manually removed any that were missed during the previous step. 

I also removed organisations where a person’s name had been inputted into the form instead of the organisation name and no organisation name was salvageable. I then converted the json into a pandas dataframe and saved it as a csv file.

#### Development trust data
In order to add development trusts to the local authority maps, I scraped a list of development trust names from the Development Trusts Association Scotland website ([here](https://dtascot.org.uk/dtas-member-network/a-z-of-members)), using the Python library BeautifulSoup4. 

I then created a dataframe from the list of names, searched for each organisation and added an associated postcode to the dataframe for a location as close to the development trust site as possible. 

I used the NRS Postcode Index to get coordinates for each of these postcodes, and exported the dataframe to a csv file.

#### Community space data
To create the community spaces dataset, a colleague and I used Google Maps searches. We searched for the terms “community centres”, “community halls”, “village halls”, “libraries”, “leisure centres”, and “citizens advice”, along with the local authority name, to get a list of community spaces for each local authority. 

We also added postcodes to this data, and used the NRS Postcode Index to get coordinates from the postcodes.

#### Other data
I downloaded SIMD data from [here](https://simd.scot/#/simd2020/BTTTFTT/9/-4.0000/55.9000/), intermediate zone boundary data for the whole of Scotland from [here](https://spatialdata.gov.scot/geonetwork/srv/eng/catalog.search#/metadata/389787c0-697d-4824-9ca9-9ce8cb79d6f5), and life expectancy data from [here](https://scotland.shinyapps.io/ScotPHO_profiles_tool/).

I wanted to include primary schools on the map using [this](https://data.gov.uk/dataset/9a6f9d86-9698-4a5d-a2c8-89f3b212c52c/scottish-school-roll-and-locations) data, as they are often places where people can meet others from their community, but after plotting the data, I realised that many of the coordinates in the dataset were slightly offset, meaning that primary schools were sometimes placed in the wrong intermediate zone.

### Data at local authority level
Once these steps were complete, I decided to break down the data by local authority, so as to make a dataset with information on intermediate zones for each local authority.

#### Business data
I downloaded business data by local authority from [here](https://www.nomisweb.co.uk/datasets/idbrlu), but it is also possible to download the whole dataset then use intermediate zone codes or names to filter local authorities. 

In order to download, I clicked “Query data”, “Begin first step of guidance”, “Some” from the dropdown on “2011 scottish intermediate zones (*2016 onwards*)”, selected a local authority from the dropdown then clicked “tick all”, then continued clicking next to get default settings until I got to the download page, where I selected the .csv format and clicked download. 

I renamed and moved the dataset to the appropriate directory (/data/*local_authority_name*/businesses_*local_authority_name*).

### Creating community asset datasets by local authority
I defined functions that would create a csv file of charities for each local authority, a csv file of mutual aid organisations in each local authority, and a csv file of development trusts in each local authority. These each took in a local authority name (to filter the larger datasets on) and a save location for the new csv.

### Getting intermediate zone information by local authority
I then wrote a function that would create the overarching dataset for each local authority (these were saved to the /data/*local_authority_name* folder, as well as an html map (these were saved to the /assets folder). 

This function took in a file path for a community spaces dataset for the local authority, a file path to the charities dataset for the local authority, a file path for the mutual aid organisations dataset for the local authority, a file path to the businesses dataset for the local authority, coordinates for the centre of the local authority (in order to correctly position the map start-point), a number to define the zoom start for the map, a local authority name, and save locations for the intermediate zone information dataset for the local authority, and the map for the local authority.
 
The function read in the postcode lookup dataset, the datazone lookup dataset the boundary data for intermediate zones in Scotland, the SIMD dataset, the life expectancy dataset, as well as the community spaces, charities, businesses, mutual aid organisations, development trusts datasets for the local authority. 

The function merged datasets that have postcodes but do not have coordinates for each community asset with the NRS Postcode Index in order to be able to plot these onto a map. 

It created a list of the intermediate zones in a local authority using the datazone lookup dataset, then selected the rows of the intermediate zone boundary dataset that corresponded to those intermediate zones. 

The function also created a list of data zones in the local authority in order to select the relevant rows of the SIMD dataset for that local authority.
 
The function filtered the SIMD dataset to get only rows where the units are equal to “Decile” (there are also rank, quintile, and vigintile units).

The function then merged the SIMD dataframe with the data zone lookup dataframe, and grouped by intermediate zone using the pandas .mean() method to compute the mean SIMD decile for a group of data zones in an intermediate zone. The function then assigned that mean SIMD decile to the relevant intermediate zone. 

Next, the function calculated the number of community spaces, charities, and businesses in each intermediate zone, as well as the number of these per 1000 people. Any missing values were replaced with the mean for the local authority.
 
The function then merged all of the dataframes to be included in the local authority intermediate zone information dataset into one pandas dataframe, and exported it to the save location provided as a function argument as a csv file.

### Creating a map for each local authority
Next, the function created a map using Folium, with an OpenStreetMap tile layer (background).

The function created geodataframes from the community spaces, charities, mutual aid organisations, development trusts, dataframes, as well as the intermediate zone information dataframe for the local authority. 

It then added marker clusters and marker layers to the map for the plottable layers, converted the coordinate reference system of the intermediate zone boundary layer to ESPG:27700, and added a highlight function and tooltips to the map for interactivity. The map was then saved at the save location specified in the function call.

### Creating decile tabls for each local authority
In the /data_generation/table_data file, I defined three functions that find the mean number of businesses, charities and community spaces per SIMD decile in each local authority. The functions took in an intermediate zone information csv file for a local authority, and saved a new csv file with the businesses, charities, or community spaces per 1000 people in each decile of the SIMD.

### Creating the Scottish Household Survey / Mutual aid organisations dataset
In the shs_mao file I created a dataframe with the number of mutual aid organisations per 100,000 people and the percentage of people who would agree with the statement “I could rely on someone in my neighbourhood to help me” in each local authority. This percentage comes from the [Scottish Household Survey](https://scotland.shinyapps.io/sg-scottish-household-survey-data-explorer/). I then saved the relevant information for each local authority to a csv file in the /data/*local_authority* folder.

### Dashboard
All of the above data was incorporated into the dashboard through maps, tables, and graphs.

## Summary

In intermediate zones across Scotland, there was a significant, medium strength positive correlation between charities per capita and community spaces per capita (*r* = 0.55, *p* < 0.05). 

There was a significant, weakly positive correlation between businesses per capita and community spaces per capita (*r* = 0.25, *p* < 0.05). 

There was also a significant, moderately positive correlation between businesses per capita and charities per capita (*r* = 0.45, *p* < 0.05).

Below is a screenshot of a facet plot showing the number of charities per 1000 people versus the number of community spaces per 1000 people in intermediate zones for each local authority

![A screenshot of a facet plot which is made up of scatter plots for each local authority. Each scatter plot shows the number of charities per 1000 people plotted against the number of community spaces per 1000 people in each intermediate zone for the local authority depicted.](/assets/images/charities_community_spaces_scatter_plot.png)

Here is a screenshot of a facet plot showing the number of charities per 1000 people versus the number of businesses per 1000 people in intermediate zones for each local authority

![A screenshot of a facet plot which is made up of scatter plots for each local authority. Each scatter plot shows the number of charities per 1000 people plotted against the number of businesses per 1000 people in each intermediate zone for the local authority depicted.](/assets/images/charities_businesses_scatter_plot.png)

Another finding that came out of this analysis is that there seem to be less charities and businesses per capita in communities defined as more deprived by the SIMD, yet more community spaces per capita in these areas. 

![A screenshot of a bar plot showing the number of charities per 100,000 people in each SIMD decile, across Scotland](/assets/images/charitiesper100k_by_simd_decile.png)

![A screenshot of a bar plot showing the number of businesses per 100,000 people in each SIMD decile, across Scotland](/assets/images/businessesper100k_by_simd_decile.png)

![A screenshot of a bar plot showing the number of community spaces per 100,000 people in each SIMD decile, across Scotland](/assets/images/community_spacesper100k_by_simd_decile.png)

Below, I outline some key points about the overarching dataset that I created, which contains a variety of information on all intermediate zones in Scotland:
 
##### Mean
- Charities per 1000 people: 2.6
- Businesses per 1000 people: 40.48
- Community spaces per 1000 people: 0.55
- Female life expectancy: 81.5
- Male life expectancy: 77.2
 
##### Maximum
- Charities per 1000 people: 28.07 (City Centre West (Aberdeen City))
- Businesses per 1000 people: 947.0 (City Centre South (Glasgow City))
- Community spaces per 1000 people: 7.12 (North and East Isles (Shetland Islands))
- Female life expectancy: 94 (Dumfermline Milesmark and Wellwood (Fife); Kirkcaldy Dunnikier (Fife); Langholm and Eskdale (Dumfries and Galloway))
- Male life expectancy: 88 (Fishcross, Devon Village and Coalsnaughton (Clackmannanshire))
 
##### Minimum
- Charities per 1000 people: 0.0 (19 intermediate zones)
- Businesses per 1000 people: 3.0 (Girvan Glendoune (South Ayrshire))
- Community spaces per 1000 people: 0.0 (267 intermediate zones)
- Female life expectancy: 71 (Drumoyne and Shieldhall (Glasgow City); Drumchapel South (Glasgow City))
- Male life expectancy: 63 (Menzieshill (Dundee City); Drumoyne and Shieldhall (Glasgow City))



# Insert rest of summary here


## Data Sources

### Charity data
Office for the Scottish Charity Register: © Crown Copyright and database right 2021. Contains information from the Scottish Charity Register supplied by the Office of the Scottish Charity Regulator and licensed under the [Open Government Licence v.3.0](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
 
Available [here](https://www.oscr.org.uk/about-charities/search-the-register/charity-register-download/).

### Postcode data
Postcode index: © Crown copyright. Data supplied by National Records of Scotland
 
Available [here](https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products/scottish-postcode-directory/2021-2).

### SIMD
Copyright Scottish Government, contains Ordnance Survey data © Crown copyright and database right 2021. 
 
Available [here](https://simd.scot/#/simd2020/BTTTFTT/9/-4.0000/55.9000/).

### Data Zone Lookup
Scottish Government, 2019, licensed under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

Available [here](https://statistics.gov.scot/data/data-zone-lookup).

### UK Business Counts
ONS Crown Copyright Reserved [from Nomis on 20 October 2021].
 
Available [here](https://www.nomisweb.co.uk/datasets/idbrlu).

### Intermediate Zone Boundaries
Copyright Scottish Government, contains Ordnance Survey data © Crown copyright and database right 2021.
 
Available [here](https://spatialdata.gov.scot/geonetwork/srv/eng/catalog.search#/metadata/389787c0-697d-4824-9ca9-9ce8cb79d6f5).

### Life expectancy data
Contains data from the Scottish Public Health Observatory.
Available [here](https://scotland.shinyapps.io/ScotPHO_profiles_tool/).

### Population estimates
Contains NRS data © Crown copyright and database right 2021.

Available [here](https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/population/population-estimates/2011-based-special-area-population-estimates/small-area-population-estimates).

### Mutual aid organisations
This dataset is likely to be partial as it relies on group members/founders putting information about the group onto the website.
 
Available [here](https://mutualaid.wiki/api/group/get).

### Development trusts
Available [here](https://dtascot.org.uk/dtas-member-network/a-z-of-members).

### Scottish Household Survey
Scottish Government, 2020, licensed under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
 
Available [here](https://scotland.shinyapps.io/sg-scottish-household-survey-data-explorer/).

### Community spaces
Data collected from Google Maps searches for “community centres”, “village halls”, “community halls”, “leisure centres”, “libraries”, “citizens advice bureau”.
