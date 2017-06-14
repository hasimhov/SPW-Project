from __future__ import unicode_literals

from django.db import models
from login.models import User
# Create your models here.
class Post(models.Model):
	text = models.CharField(max_length=300)
	user = models.ForeignKey(User)
	image = models.ImageField(blank=True)
	def __str__(self):
		return self.text

class Reply(models.Model):
	text = models.CharField(max_length=300)
	user = models.ForeignKey(User)
	image = models.ImageField(blank=True)
	Repost = models.ForeignKey(Post)
	def __str__(self):
		return self.text

	
