# Estimating the impacts of CA SB 827
In January 2018 Califonria State Senator Wiener introduced [Senate Bill 827: Planning and zoning: transit-rich housing bonus](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201720180SB827) or for short SB 827. This bill has the potential to be the most impact housing bill the state has passed since 1978's Prop 13 Digitize Zoning Codes and as such there's been a lot of public response to the bill. This repo was started by the [Policy Club](http://policyclub.io) to estimate the specific impacts of SB 827 on the city Los Angeles. This repo is set up such that contributing a few files will extend this analysis estimate the impacts of other California cities.

## Mapping the impacts 

In order to create the map for a city, we need 3 things: (1) a Zoning file as a geojson (2) a zoning attributes file and (3) transit data, specifically a high quality transit definition. 

### (1) Zoning File (GeoJSON)

We used the City of LA's zoning file, downloaded as `.geojson` from the [LA City Geohub](geohub.lacity.org). The zoning file must contain an attribute called `zone`, which will be used to join it with the zoning attributes file.

### (2) Zoning Attributes Table (CSV)
For each unique `zone` type in the zoning spatial file, you'll need to describe in an attributes table. In the zoning-metadata.csv file, you'll need to provide True/False data for six new fields for SB 827. 

+ `sb_827_parking`: _more info needed here_
+ `sb_827_FAR`:
+ `sb_827_res_density`:
+ `sb_827_height_quarter_mile`:
+ `sb_827_height_half_mile`:
+ `sb_827_non_res`: True if the zone is a non-residential type (ie, Industrial, Park, Government Center).

Example table (only first three, and last six columns shown)

zone | zone type | use | sb_827_parking | sb_827_FAR | sb_827_res_density | sb_827_height_quarter_mile | sb_827_height_half_mile | sb_827_non_res
----
Agricultural | A1 | Agricultural |
One-Family Residential | R1 | One-Family Dwelling
Multiple Residential | R2 | Two Family Dwellings
Manufacturing | M2 | Light Industrial

For a full example, check out the file in `los-angeles/los-angeles/zoning-metadata.csv`

### (3) Transit Data (GeoJSON)
We use [Southern California Association of Governments (SCAG)'s](http://www.scag.ca.gov/) high quality transit definition from 2012 for Southern California and will be updating it as the bill changes. We'll take care of locating this if you're in SCAG's area. 

## Contributing 

Submit updates to the spec in the form of Pull Requests. 

Questions? Comments? Open an issue and we'll work with you to help get your city analyzed. 
