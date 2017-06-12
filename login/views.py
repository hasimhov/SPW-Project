# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import User
# Create your views here.
def signUpHandler(request):
	# firstname = request.POST[first_name]
	# lastname = request.POST[last_name]
	# password = request.POST[password]
	# emailId = request.POST[email]
	# phoneNum = request.POST[phone]
	# u = User(firstname=firstname, lastname =lastname,password=password,emailId=emailId,phoneNumber=phoneNum)
	# u.save()
	return render(request,'index.html',{})

def loginHandler(request):
	email = request.POST['email1']
	passwd = request.POST['passwd1']
	password1 = user.objects.get(password)