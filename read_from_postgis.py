import geopandas as gpd
import psycopg2


con = psycopg2.connect(database="transit-rich", user="hunterowens",host="localhost")

sql= "select * from low_rise_with_zoning LIMIT 10"

aff_prop  =gpd.GeoDataFrame.from_postgis(sql,con,geom_col='wkb_geometry')
