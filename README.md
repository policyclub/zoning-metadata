# zoning-metadata
Digitize Zoning Codes to estimate the Impact of SB 827.

## Contributing 

In order to add your city, we'll need 3 things: 1) a Zoning geojson file 2) a zoning metadata mile and 3) a high quality transit definition. We use SCAG's for Sothern California and will be updating it as the bill changes. 

### Zoning File

We used the City of LA's zoning file, downloaded as `.geojson` from the Geohub. It must contain a attribute called `zone`, which we use to join it with our metadata file. 

### Zoning Metadata 
For each unique zone type in zoning, you'll need to describe in metadata. In the zoning-metadata.csv file, you'll need to provide True/False data for 5 different new catagories. 

`sb_827_parking`, `sb_827_FAR`, `sb_827_res_density`, `sb_827_height_quarter_mile`, `sb_827_height_half_mile` and `sb_827_non_res`. The first four are qualifications for each zonetype and then `sb_827_non_res` is for properties that do not have any residental zoning attached (ie, Industrial, Park, Government Center). For an example, check out the file in `los-angeles/los-angeles/zoning-metadata.csv`. 

Submit updates to the spec in the form of Pull Requests. 

### Transit Data
We'll take care of locating this if you're in SCAG's area. 

## Contributing 

Questions? Comments? Open an issue and we'll work with you to help get your city analyzed. 
