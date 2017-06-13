# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
# Create your views here.
def signUpHandler(request):
	print type(request)
	request.path+='/check'
	print request.path
	return render(request,'Signup.html',{})

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
	t=loader.get_template('index.html')

	return HttpResponse(t.render({},request))

def check(request):

	firstname = request.POST['name']
	dob = request.POST['bdate']
	password = request.POST['pwd']
	emailId = request.POST['email']
	phoneNum = request.POST['phoneno']
	u = User(firstName=firstname,password=password,emailId=emailId,phoneNumber=phoneNum,dob=dob	)
	u.save()
	return render(request,'index.html',{'name':firstname})



