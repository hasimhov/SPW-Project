# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def signUpHandler(request):
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
		return redirect("/login/signup")
	if user1.password!=passwd:
		return redirect("/login/signup")
	print " password correct"
	request.session['email']=email
	return redirect("/wall/")

def login(request):
	t=loader.get_template('index.html')
	# email=request.session['email']
	# email=""
	return HttpResponse(t.render({},request))

def check(request):

	firstname = request.POST['name']
	dob = request.POST['bdate']
	password = request.POST['pwd']
	emailId = request.POST['email']
	phoneNum = request.POST['phoneno']
	u = User(firstName=firstname,password=password,emailId=emailId,phoneNumber=phoneNum,dob=dob	)
	u.save()
	# del request.session
	
	request.session['email']=emailId
	return redirect("/wall/")
	# return render(request,'check1.html',{'name' : emailId})


def check1(request):
	return render(request,'check1.html',{})



