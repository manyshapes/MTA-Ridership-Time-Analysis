# MTAPD Ridership Time Analysis
Finding Off Peak Hours to Maximize Public Health Interests for the New York City Metropolitan Transportation Authority
This project was performed as piece of a course taught by [@metis](https://github.com/thisismetis), San Francisco branch.  

## Objective
Our objective is to incentivize use of MTA transit systems during lower ridership times in service of public health. We propose discounting fare prices at specific times intervals and stations, where these decisions will decided based on data visualization results of foot traffic.

### Dataset
MTA's turnstile data is publicly available information, updated every Saturday. The data source can be found [here.](http://web.mta.info/developers/turnstile.html) Each turnstile, cataloguing entrances and exits of MTA passengers, updates its records every four hours. Passage numbers are a cummulative running total. These turnstiles are then reset periodically for system maintenance. These resets can be viewed as a unique quirk of this dataset.

### Tools Used
**Jupyter Notebooks** was used as an interface through which **Python** was employed.
**Pandas** was used for data access & transformation. **Matplotlib** and **Seaborn** were both used for plotting. **Numpy** is used for math that handles quirky outliers.

## Start Here 
FootTraffic Calculations Final.ipynb has all code needed to perform the exploratory data analysis. This file includes, in following order, data retrieval (online & locally), data processing, relevant findings & plotting. Original data used for this data analysis is available within the .csv files. 

### Findings
MTA passengers may know that overall there is generally less riders before 9 am, as well as on the weekends. Early afternoons have less ridership than travels after 3 pm.

These general rules of thumb must be examined more on a station by station basis--in future works, line by line basis may also be possible. Viewed within the 5 stations we've pinpointed as intakers of great foot traffic, times of peak use very greatly. 

- Fulton St & 86th Station both follow our general rule of thumb, early afternoons and especially early mornings are safer.
- 42nd Grand Central's mornings are safer with steady traffic throughout the day.
- 59th St Station passengers gradually increase from early morning to late afternoon.
- 34th St Penn Station sees the greatest influx of passengers in the morning, riders can expect less passengers between late morning and midday.


#### Done By:

|Name     |  Slack Handle   | 
|---------|-----------------|
| Vasana Sihamaya(https://github.com/vsihamaya) | @vsihamaya  |
| Brian Nguyen(https://github.com/bt-nguyen/) | @bt-nguyen  |
| Lauren Faulds (https://github.com/manyshapes/) | @manyshapes  |

Please reach out to @manyshapes if you have any questions or comments relating to this project. 
