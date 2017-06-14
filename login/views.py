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
	email = request.POST['username']
	passwd = request.POST['password']
	#print '\n\n'+email+'\n\n'
	#print User.objects.get(firstName = "sds" )
	try:
		print "HI"
		#print User.objects.get(id = 3)
		user1 = User.objects.get(emailId=str(email))

	except:
		print "incorrect username"

		request.path = (request.path).replace("check1/","signup/")
		print request.path
		return render(request,"Signup.html",{})
	if user1.password!=passwd:
		print "incorrect password"
		request.path = (request.path).replace("check1/","signup/")
		return render(request,"Signup.html",{})
	print " password correct"
	# request.session['email']=email
	return render(request,'check1.html',{'name' : email})

def login(request):
	t=loader.get_template('index.html')
	email=request.session['email']
	# email=""
	return HttpResponse(t.render({'name':email},request))

def check(request):

	firstname = request.POST['name']
	dob = request.POST['bdate']
	password = request.POST['pwd']
	emailId = request.POST['email']
	phoneNum = request.POST['phoneno']
	u = User(firstName=firstname,password=password,emailId=emailId,phoneNumber=phoneNum,dob=dob	)
	u.save()
	return render(request,'index.html',{'name':firstname})

def check1(request):
	return render(request,'check1.html',{})



