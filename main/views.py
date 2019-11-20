from django.shortcuts import render
from django.http import HttpResponse
from .models import Water
import requests



def homepage(request):
	response = requests.get('https://api.mediatek.com/mcs/v2/devices/DIrbqT7X/datachannels/2/datapoints')
	data = response.json()
	return render(request, 'main/home.html',{
		'val': data['message']
		#'val': data['dataChannels']['dataPoints'][0]['value']
		})
	"""return render(request=request, 
				  template_name="main/home.html",
				  context={"water": Water.objects.all})#refer to all tutorial objects as "tutorials" in home.html

"""