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
	for frnd in frnds1:
		posts.append(frnd.sender.post_set.all())
	for frnd in frnds2:
		posts.append(frnd.receiver.post_set.all())
	for post in posts:
		for i in range(len(post)):
			postsrep.append({'post':post[i],'replies':post[i].reply_set.all()})
	context = {
		'user':user,
		'posts':postsrep,
		'frnds':frnds,
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
	sender=request.POST['sender']
	receiver = User.objects.get(emailId=str(request.session['email']))
	friend=True
	#U needs to be found First ,me Have to read query
	#u=Friends(sender=sender,receiver=receiver,friend=friend)
	#u.save()
	return redirect('/wall/')
def freq(request):
	sender = User.objects.get(emailId=str(request.session['email']))
	receiver=request.POST['receiver']
	friend=False
	#u=Friends(sender=sender,receiver=receiver,friend=friend)
	#u.save()
	return redirect('/wall/')

def profile(request,emailId):
	user = User.objects.get(emailId=emailId)
	posts=user.post_set.all()
	postsrep=[]
	for i in range(len(posts)):
			postsrep.append({'post':posts[i],'replies':posts[i].reply_set.all()})
	context = {
		'user':user,
		'posts':postsrep,
	}
	return render(request,'/post/wall.html',context)