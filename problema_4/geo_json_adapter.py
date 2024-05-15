from geo_data import IntGeoData
from kml_library import KMLLibrary

class GeoJSONAdapter (IntGeoData):
    def __init__(self,geojson_data):
       self.geojson_data = geojson_data
       self.kml_library = KMLLibrary()

    def load_data(self,data):
        print("converting GeoJSON to KML")
        kml_data=self.convert_geojson_to_kml(data)
        self.kml_library.load_kml(kml_data)

    def display_map(self):
        self.kml_library.display_kml_map()

    def convert_geojson_to_kml(self,geojson_data):
        print("GeoJSON converted to KML",geojson_data)
        kml_convert_data=geojson_data
        return kml_convert_data
  





