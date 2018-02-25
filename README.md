# Estimating the impacts of CA SB 827
In January 2018 California State Senator Wiener introduced [Senate Bill 827 Planning and zoning: transit-rich housing bonus](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180SB827) or for short SB 827. This bill has the potential to be the most impactful housing bill the state has passed since 1978's Prop 13 and as such there's been a lot of public response to the bill. This repo was started by the [Policy Club](http://policyclub.io) to estimate the specific impacts of SB 827 on the City of Los Angeles. This repo is set up such that by contributing a few files one could extend this analysis to estimate the impacts of SB 827 on other California cities.
## Data for the Map 

In order to create the map for a city, we need 3 things: (1) a Zoning file as a geojson (2) a zoning attributes file and (3) transit data, specifically a high quality transit definition. 

### (1) Zoning File (GeoJSON)

We used the City of LA's zoning file, downloaded as `.geojson` from the [LA City Geohub](geohub.lacity.org). The zoning file must contain an attribute called `zone`, which will be used to join it with the zoning attributes file.

### (2) Zoning Attributes Table (CSV)
For each unique `zone` type in the zoning spatial file, you'll need to describe it in an attributes table. In the zoning-metadata.csv file, you'll need to provide True/False data for six new fields for SB 827. 

+ `sb_827_parking`: True if parking requirements are wavied 
+ `sb_827_FAR`: True if the FAR requirements are changed. 
+ `sb_827_res_density`: True if there are requirements on minimum residental density that are removed. 
+ `sb_827_height_quarter_mile`: True if the height limit is increased if within 1/4 quarter mile of a trasit stop.  
+ `sb_827_height_half_mile`: Same as above, but for the 1/2 mile heights, rather than the quarter mile heights. 
+ `sb_827_non_res`: True if the zone is a non-residential type (ie, Industrial, Park, Government Center). Additionaly 

Example table (only first three, and last six columns shown)

| zone | zone type | use | sb_827_parking | sb_827_FAR | sb_827_res_density | sb_827_height_quarter_mile | sb_827_height_half_mile | sb_827_non_res |
|-|-|-|-|-|-|-|-|-|
| Agricultural | A1 | Agricultural |||||||
|One-Family Residential | R1 | One-Family Dwelling|
|Multiple Residential | R2 | Two Family Dwellings|
|Manufacturing | M2 | Light Industrial|

For a full example, check out the file in `los-angeles/los-angeles/zoning-metadata.csv`

### Zoning.Space

As of 25 Febuary 2018, Zoning Data is now being populatd at the Zoning.Space Repo. It is a submodule of this repo, we use it to generate SB 827 specific shapefiles. Checkout more at [Zoning.Space](https://github.com/zoningspace/zoning.space.git)

### (3) Transit Data (GeoJSON)
We use Transit Data that we have gotten data from their GTFS feeds and applied a filter for meeting SB 827 standards.  

## Contributing 

Submit updates to the spec in the form of Pull Requests. 

Questions? Comments? Open an issue and we'll work with you to help get your city analyzed. 
