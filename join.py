import pandas as pd
import geopandas as gpd

zoning = gpd.read_file('./los-angeles/los-angeles/zoning.geojson')

zoning_metadata = pd.read_csv('./los-angeles/los-angeles/zoning-metadata.csv')

zoning['zone'] = zoning.ZONE_CLASS

merged = zoning.merge(zoning_metadata, on='zone')

print("Lost {} parcels in merged from original list of {}".format(len(zoning) - len(merged),
                                                                   len(zoning)))
query_params = ['sb_827_parking', 'sb_827_FAR', 'sb_827_res_density', 
               'sb_827_height_quarter_mile','sb_827_height_half_mile']

qual_prop = merged[merged[query_params].any(axis=1)]

print("num of qualified zones is ", len(qual_prop))
qual_prop = qual_prop[qual_prop['sb_827_non_res'] == False]

print("num of qualified minus non res is ", len(qual_prop))
hqtas = gpd.read_file('./transit-service/SCAG-hqta.geojson')
aff_prop = gpd.sjoin(merged, hqtas, op='intersects', how='inner')

height_changes = aff_prop[aff_prop['sb_827_height_quarter_mile'] == True]
parking_changes = aff_prop[aff_prop['sb_827_parking'] == True]
res_density_increate = aff_prop[aff_prop['sb_827_res_density'] == True]

height_changes.to_file('./outputs/height.geojson', driver='GeoJSON')
parking_changes.to_file('./outputs/parking_changes.geojson', driver='GeoJSON')
res_density_increate.to_file('./outputs/res_density.geojson', driver='GeoJSON')
