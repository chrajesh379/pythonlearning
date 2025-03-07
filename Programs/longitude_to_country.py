from geopy.geocoders import Nominatim

def get_county_name(latitude, longitude):
    geolocator = Nominatim(user_agent="geo_app")
    coordinates = f"{latitude}, {longitude}"
    location = geolocator.reverse(coordinates)
    
    if location:
        address = location.raw['address']
        if 'county' in address:
            return address['county']
        elif 'state_district' in address:
          return address['state_district']
        else:
            return "County name not found"
    else:
        return "Location not found"

# Example usage:
latitude = 34.0522  # Example latitude
longitude = -118.2437  # Example longitude

county_name = get_county_name(latitude, longitude)
print(f"The county name is: {county_name}")
