from geo_json_adapter import GeoJSONAdapter

def main():
    # Datos en formato GeoJSON
    geojson_data = {"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [0, 0]}}]}
    
    # Crear adaptador y cargar datos
    adap = GeoJSONAdapter(geojson_data)
    adap.load_data(geojson_data)
    # Mostrar el mapa
    adap.display_map()

if __name__ == "__main__":
    main()
    
