# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
# Create your views here.
def signUpHandler(request):
	firstname = request.POST[first_name]
	lastname = request.POST[last_name]
	password = request.POST[password]
	emailId = request.POST[email]
	phoneNum = request.POST[phone]
	u = User(firstname=firstname, lastname =lastname,password=password,emailId=emailId,phoneNumber=phoneNum)
	u.save()
	return render(request,'index.html',{})

def loginHandler(request):
	email = request.POST['email1']
	passwd = request.POST['passwd1']
	try:
		user1 = user.objects.get(emailId=email)
	except:
		return render(request,index.html,{})
	if user1.password!=passwd:
		return render(request,index1.html,{})
def login(request):
	t=loader.get_template('Signup.html')
	return HttpResponse(t.render({},request))
