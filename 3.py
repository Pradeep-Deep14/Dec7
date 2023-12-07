from geopy.geocoders import Nominatim

#create the geolocator object with a user-agent

geolocator=Nominatim(user_agent="geoapiExercises")

#Get the city name from the user

place= input ("Enter City Name: ")

#Geocode the Location

location =geolocator.geocode(place)

#print the geolocation details
print(location)