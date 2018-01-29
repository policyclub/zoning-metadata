import shapely.geometry
import shapely.ops
import json

# convert the shapes used by the webapp to shapely shapes
def webappToShape (shp):
    return shapely.geometry.shape({
        'type': 'MultiPolygon',
        'coordinates': [[[[ll['lng'], ll['lat']] for ll in poly]] for poly in shp]
    })

# Load SB 827 data
#with open(join(path, '..', '..', 'data', 'low_rise_shape.json')) as lowRiseFd:
with open('./transit-service/data/low_rise_shape.json') as lowRiseFd:
    lowRise = webappToShape(json.load(lowRiseFd))

#with open(join(path, '..', '..', 'data', 'high_rise_shape.json')) as highRiseFd:
with open('./transit-service/data/high_rise_shape.json') as highRiseFd:
    highRise = webappToShape(json.load(highRiseFd)).buffer(1e-8)

affectedArea = lowRise.union(highRise)

with open('./transit-service/data/affected.geojson', 'w') as f:
    f.write(json.dumps(shapely.geometry.mapping(affectedArea)))

with open('./transit-service/data/high_rise_affected.geojson', 'w') as f:
    f.write(json.dumps(shapely.geometry.mapping(highRise)))


