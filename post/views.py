from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post,Reply,User,Friends
# Create your views here.
def wall(request):
	user = User.objects.get(emailId=str(request.session['email']))
	postsrep = []
	frreq = user.receiver.all().filter(friend=False)
	frnds1 = user.receiver.all().filter(friend=True)
	frnds2 = user.sender.all().filter(friend=True)
	frnds = frnds1 | frnds2
	posts = []	
	actfrnds=[]
	for frnd in frnds1:
		posts.append(frnd.sender.post_set.all())
	for frnd in frnds2:
		posts.append(frnd.receiver.post_set.all())
	for frnd in frnds:
		if frnd.sender.emailId==request.session['email']:
			actfrnds.append(frnd.receiver)
		else:
			actfrnds.append(frnd.sender)
	for post in posts:
		for i in range(len(post)):
			postsrep.append({'post':post[i],'replies':post[i].reply_set.all()})
	context = {
		'user':user,
		'posts':postsrep,
		'frnds':actfrnds,
		'frreq':frreq,
	}
	return render(request,'post/hello.html',context)
def post(request):
	text=request.POST['posts']
	user = User.objects.get(emailId=str(request.session['email']))
	u=Post(text=text,user=user)
	u.save()
	return redirect('/wall/')
def reply(request):
	text = request.POST['comment']
	user = User.objects.get(emailId=str(request.session['email']))
	postid = request.POST['postid']
	post = Post.objects.get(id=int(postid))
	u = Reply(text=text, user=user, Repost=post)
	u.save()
	return redirect('/wall/')
def freqapt(request):
	u=Friends.objects.get(id=request.POST['id'])
	u.friend=True
	u.save()
	return redirect('/wall/')
def freq(request):
	sender = User.objects.get(emailId=str(request.session['email']))
	receiver=User.objects.get(emailId=str(request.POST['email1']))
	friend=False
	u=Friends(sender=sender,receiver=receiver,friend=friend)
	u.save()
	return redirect('/wall/allusers')
def allusers(request):
	user = User.objects.get(emailId=request.session['email'])
	users=[]
	friends = Friends.objects.all()
	for friend in friends:
		if friend.sender.emailId==user.emailId or friend.receiver.emailId==user.emailId:
			if friend.sender.emailId==user.emailId:
				users.append(friend.receiver)
			else:
				users.append(friend.sender)
	totusers = User.objects.all()
	print totusers	
	for us in totusers:
		if us in users:
			totusers=totusers.exclude(emailId=us.emailId)
	totusers=totusers.exclude(emailId=request.session['email'])
	context={
		'user':user,
		'users':totusers,
	}
	return render(request,'post/friends.html',context)
				

				


def profile(request,emailId):
	user = User.objects.get(emailId=emailId)
	posts=user.post_set.all()
	postsrep=[]
	cuser = User.objects.get(emailId=str(request.session['email']))
	name=cuser.firstName
	email=request.session['email']
	for i in range(len(posts)):
			postsrep.append({'post':posts[i],'replies':posts[i].reply_set.all()})
	context = {
		'user':user,
		'posts':postsrep,
		'email':email,
		'name':name,
	}
	return render(request,'post/wall.html',context)

def settings(request):
	user = User.objects.get(emailId=str(request.session['email']))
	context={
		'user':user
	}
	return render(request,'post/settings.html',context)
def logout(request):
	del request.session['email']
	return redirect('/login/signup')
	#is the url correct
def checker(request):
	user = User.objects.get(emailId=str(request.session['email']))
	firstname = request.POST['name']
	password = request.POST['pwd']
	opassword = request.POST['opwd']
	phoneNum = request.POST['phoneno']
	if opassword==user.password:
		user.firstName=firstname
		if len(password)>0:
			user.password=password
		user.phoneNumber=phoneNum
		user.save()
		return redirect('/wall/')
	else:
		return render(request,'post/error.html')
