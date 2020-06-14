from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from .forms import LikeVideoForm
import requests
from .  import models 


def index(request):
	search_word = request.GET.get('q')

	if search_word:
		URL = 'https://www.googleapis.com/youtube/v3/search'

		PARAMS = {
		    'key': 'AIzaSyAG_ZoDM24jTIl1YLPlE7ftvxmkjKZ7bJE',
		    'part': 'snippet',
		    'type': 'video',
		    'maxResults': '9',
		    'q': search_word,
		}
		if(request.method == 'POST'):
			form = LikeVideoForm(request.POST)
			form.save()

		response = requests.get(URL, PARAMS)
		all_videos = []

		if response.ok:
		    result = response.json()
		    for item in result['items']:
		    	video = {
		    		'id': item['id']['videoId'],
		    		'title': item['snippet']['title'],
		    		'description': item['snippet']['description'],
		    		'channel_title': item['snippet']['channelTitle'],
		    		'preview_url': item['snippet']['thumbnails']['medium']['url']
		    	}
		    	all_videos.append(video)

		    context = {
				'found_videos': all_videos
			}
		    return render(request, 'video/index.html', context)
		else:
			return render(request, 'video/index.html')

	return render(request, 'video/index.html')
