from .models import LikeVideo
from django.forms import ModelForm

class LikeVideoForm(ModelForm):
	class Meta:
		model = LikeVideo
		fields = ['title']
		fields = ['video_id']
		fields = ['duration']
		fields = ['thumbnail']
		
		