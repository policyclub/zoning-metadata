import pandas as pd
import geopandas as gpd

zoning = gpd.read_file('./los-angeles/los-angeles/zoning.geojson')

zoning_metadata = pd.read_csv('./los-angeles/los-angeles/zoning-metadata.csv')

zoning['zone'] = zoning.ZONE_CLASS

merged = zoning.merge(zoning_metadata, on='zone')

print("Lost {} parcels in merged from original list of {}".format(len(zoning) - len(merged),
                                                                   len(zoning)))
qual_params = ['sb_827_parking', 'sb_827_FAR', 'sb_827_res_density', 
               'sb_827_height_quarter_mile','sb_827_height_half_mile']

qual_prop = merged[qual_params]
qual_prop = qual_prop[qual_prop.sb_827_non_res == False]

hqtas = gpd.read_file('./transit-service/SCAG-hqta.geojson')
aff_prop = gpd.sjoin(merged, hqtas, op='intersects', how='inner')

aff_prop.to_file('./la.geojson', driver='GeoJSON')
