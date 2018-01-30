#!/bin/sh

set -e

mapshaper outputs/res_density.geojson -simplify 1% -o outputs/res_density-simple.geojson

mapshaper outputs/height_85.geojson -simplify 1% -o outputs/height-simple.geojson
mapshaper outputs/parking_changes.geojson -simplify 1% -o outputs/parking_changes-simple.geojson
