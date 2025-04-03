import geopandas as gpd

# Ensure the file path is correct
file_path = r"C:/Users/cmcgrane/Downloads/hotosm_gbr_populated_places_points_gpkg/hotosm_gbr_populated_places_points_gpkg.gpkg"

# Read the file
pop_den = gpd.read_file(file_path)

# Print the data
print(pop_den)
