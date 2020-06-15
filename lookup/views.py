from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=CC23104B-8F07-4D8A-BA02-15BBCD648B17")

	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = "Error..."

	return render(request, 'home.html',{'api':api}) 	

def about(request):
	return render(request, 'about.html',{}) 	