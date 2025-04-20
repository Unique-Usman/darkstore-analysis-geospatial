import json

# Specify the keys you want to keep in the properties
keys_to_keep = ["NAME", "zone_category", "ZONE_ASSIGNED", "ASSIGNMENT_CONFIDENCE"]

# Load the original GeoJSON file
with open('newdelhibuildings_complete_zones.geojson', 'r') as f:
    geojson_data = json.load(f)

# Process each feature to retain only the desired keys in properties.
for feature in geojson_data['features']:
    new_properties = {}
    # Option 1: Only include keys if they exist
    for key in keys_to_keep:
        if key in feature['properties']:
            new_properties[key] = feature['properties'][key]
    # Option 2: Alternatively, if you want the key to exist with a default value (None) even if missing,
    # you can use the code below:
    # for key in keys_to_keep:
    #     new_properties[key] = feature['properties'].get(key)
    
    feature['properties'] = new_properties

# Save the updated GeoJSON into a new file
with open('newdelhibuildings_complete_zones_cleaned.geojson', 'w') as f:
    json.dump(geojson_data, f, indent=4)

print("The cleaned GeoJSON has been saved as 'cleaned.geojson'.")
