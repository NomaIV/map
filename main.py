import folium
from IPython.display import display

# Define the center of the map
map_center = [-29.8587, 31.0218]

# Create the Folium Map object
my_map = folium.Map(location=map_center, zoom_start=12)

# Add a marker to the map
folium.Marker(
    [-29.8587, 31.0218],
    popup="Durban",
    icon=folium.Icon(color="black", icon="info-sign")
).add_to(my_map)

# Save the map to an HTML file
my_map.save("durban_map.html")

# Display the map in the notebook (optional)
display(my_map)
