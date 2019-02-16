import urllib
import requests
import webbrowser
import geocoder
places_key = "AIzaSyD7fecjFooqc9A5tL4t5r4c6O29NFIXptk"
maps_key = "AIzaSyA0cTFGvgYFuE95Him13uqTacIpI8Terlw"

def get_loc(sel):
	r = geocoder.maxmind('me').json
	if sel==0:
		print("Your current location is : "+r['address'])
		return r['city']
	else:
		return r['country']

def poi(city):
	url="https://maps.googleapis.com/maps/api/place/textsearch/json?query="+city+"+point+of+interest&language=en&key="+places_key
	json_data=requests.get(url).json()
	print("Points of interest near your location:")
	#print(json_data)
	for i in range(0,len(json_data['results'])):
		print("\n",i+1,". ",json_data['results'][i]['name'])
		print(json_data['results'][i]['formatted_address'])

def dosearch():
	base_add='https://maps.googleapis.com/maps/api/geocode/json?'
	url=base_add + urllib.parse.urlencode({'address':input('Enter your Google Maps search query: '),'region':get_loc(1),'key':maps_key})
	json_data=requests.get(url).json()
	#print(json_data)

	if json_data['status']=="INVALID_REQUEST":
		print("Invalid search request! Please Try Again.")
		main()
	elif json_data['status']=="ZERO_RESULTS":
		print("Sorry! No Results Found. Please Try Again.")
		main()
	elif json_data['status']=="UNKNOWN_ERROR":
		print("Server Error!. Please Try Again.")
		main()
	else:
		print("\n",json_data['results'][0]['formatted_address'])
		print("\nLatitude and Longitude:")
		print(json_data['results'][0]['geometry']['location']['lat'])
		print(json_data['results'][0]['geometry']['location']['lng'])
		print("\nThe place is of type:",json_data['results'][0]['types'][len(json_data['results'][0]['types'])-1].replace('_',' '))
		ch=int(input("\nPlease Enter Choice\n1. Open in google maps\n2. Get points of interest near this location\n"))
		if ch==1:
			open_brow(json_data['results'][0]['place_id'])
		elif ch==2:
			poi(json_data['results'][0]['address_components'][0]['long_name'])

def open_brow(place_id):
	url="https://www.google.com/maps/place/?q=place_id:"+place_id
	webbrowser.open(url,new=2)

def main():
	print("Please Enter Your Choice:\n")
	ch=int(input("1. Get current location and local points of interest\n2. Google Maps Enquiry\n"))
	if ch==1:
		poi(get_loc(0))
	elif ch==2:
		dosearch()
		main()
	else:
		print("Wrong Choice! Please Enter Again.")
		main()
if __name__ == '__main__':
	main()
# curl -d @your_filename.json -H "Content-Type: application/json" -i "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyA0cTFGvgYFuE95Him13uqTacIpI8Terlw"
