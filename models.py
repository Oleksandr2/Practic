import datetime
from django.db import models

class LikeVideo(models.Model):
	title = models.TextField('название')
	video_id = models.TextField('айди')
	duration = models.TextField('время')
	thumbnail = models.TextField('картинка')
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Понравившееся видео'
		verbose_name_plural = 'Понравившееся видео'