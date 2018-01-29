import pandas as pd
import geopandas as gpd
import os 
import shutil

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
hqtas = gpd.read_file('./transit-service/data/affected.geojson')

print("loading areas")
quarter_mile_area = gpd.read_file('./transit-service/data/high_rise_affected.geojson')

print("merging data")

aff_prop = gpd.sjoin(qual_prop, hqtas, op='intersects', how='inner')
aff_prop_quarter = gpd.sjoin(qual_prop, quarter_mile_area, op='intersects', how='inner')


print("making difference dataframes")
height_changes_85 = aff_prop_quarter[aff_prop_quarter['sb_827_height_quarter_mile'] == True]
height_changes_45 = aff_prop[aff_prop['sb_827_height_half_mile'] == True]
parking_changes = aff_prop[aff_prop['sb_827_parking'] == True]
res_density_increate = aff_prop[aff_prop['sb_827_res_density'] == True]

print("writing files")
if os.path.exists('./outputs'):
    shutil.rmtree('./outputs')
    os.mkdir('./outputs')

def gdf_bool_to_int(gdf):
    """For a given GeoDataFrame, returns a copy that
    recasts all `bool`-type columns as `int`.

    GeoDataFrame -> GeoDataFrame"""
    df = gdf.copy()
    coltypes = gpd.io.file.infer_schema(df)['properties']
    for c in coltypes.items():
        if c[1] == 'bool':
            colname = c[0]
            df[colname] = df[colname].astype('int')
    return df

gdf_bool_to_int(height_changes_85).to_file('./outputs/height_85.geojson', driver='GeoJSON')
gdf_bool_to_int(height_changes_45).to_file('./outputs/height_45.geojson', driver='GeoJSON')
gdf_bool_to_int(parking_changes).to_file('./outputs/parking_changes.geojson', driver='GeoJSON')
gdf_bool_to_int(res_density_increate).to_file('./outputs/res_density.geojson', driver='GeoJSON')
