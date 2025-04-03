import geopandas as gpd
import pandas as pd
import folium
import numpy

#https://www.nomisweb.co.uk/sources/census_2021_od
data = pd.read_csv("C:/Users/cmcgrane/Downloads/odwp03ew/ODWP03EW_MSOA.csv")
#print(data.head())

flows = data.groupby(['Middle layer Super Output Areas code', 'MSOA of workplace code', 'Sex (2 categories) label']).size().reset_index(name='count')
flows = flows.rename(columns={"Middle layer Super Output Areas code": "origin_msoa", "MSOA of workplace code": "destination_msoa", "Sex (2 categories) label": "sex"})


#https://www.data.gov.uk/dataset/677a5164-3a9e-4752-b8e6-5744d2b280ec/middle-layer-super-output-areas-december-2021-boundaries-ew-bgc-v3
msoa = gpd.read_file("C:/Users/cmcgrane/Downloads/msoa.gpkg")

#https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london
gl_boundary = gpd.read_file("C:/Users/cmcgrane/Downloads/gla/gla/London_GLA_Boundary.shp")

msoa = msoa.clip(gl_boundary)

merge = msoa.merge(flows, left_on='MSOA21CD', right_on='origin_msoa', how='left')

merge = merge.head(2000)

# Define colors for men and women
colors = {'Male': 'blue', 'Female': 'pink'}



centroid = msoa.geometry.centroid

m = folium.Map(tiles="cartodb positron", location=[51.0260617, -1.3993741], zoom_start=10)

folium.GeoJson(msoa).add_to(m)
# for _, row in merge.iterrows():
#     folium.CircleMarker(
#         location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
#         radius=row['count'] / 100,  # Adjust radius as needed
#         color=colors[row['sex']],
#         fill=True,
#         fill_color=colors[row['sex']],
#         fill_opacity=0.6,
#         popup=f"Count: {row['count']}, Sex: {row['sex']}"
#     ).add_to(m)

# # Save the map
m.save('C:/Users/cmcgrane/Downloads/msoa_flows_map.html')
