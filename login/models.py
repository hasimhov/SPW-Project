# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	emailId = models.EmailField(max_length=30, primary_key = True)
	password = models.CharField(max_length=20)
	dob = models.DateField(blank=True)
	proficPic = models.ImageField(blank=True)
	phoneNumber = models.CharField(max_length=10)
	def __str__(self):
		print self.emailId
