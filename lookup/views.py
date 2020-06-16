from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":
		zipCode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipCode + "&distance=25&API_KEY=CC23104B-8F07-4D8A-BA02-15BBCD648B17")

		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50) Air Quality is considered satisfactory, and air pollution posses little or no risk"
			category_color = "good"  

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 - 100) Although general public is not likely to be affected"
			category_color = "moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
			category_description = "(151 - 200)"
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy": 
			category_description = "(201 - 300)"
			category_color = "unhealty"

		elif api[0]['Category']['Name'] == "Very Unhealthy" :
			category_description = "(301 - 500)"
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(above 500) "
			category_color = "hazardous"

		return render(request, 'home.html',{'api':api,'category_description': category_description, 'category_color':category_color}) 	
		

	else:

		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=CC23104B-8F07-4D8A-BA02-15BBCD648B17")

		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50) Air Quality is considered satisfactory, and air pollution posses little or no risk"
			category_color = "good"  

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 - 100) Although general public is not likely to be affected"
			category_color = "moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
			category_description = "(151 - 200)"
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy": 
			category_description = "(201 - 300)"
			category_color = "unhealty"

		elif api[0]['Category']['Name'] == "Very Unhealthy" :
			category_description = "(301 - 500)"
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(above 500) "
			category_color = "hazardous"

		return render(request, 'home.html',{'api':api,'category_description': category_description, 'category_color':category_color}) 	

def about(request):
	return render(request, 'about.html',{}) 	