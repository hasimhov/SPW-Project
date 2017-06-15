from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post,Reply,User,Friends
# Create your views here.
def wall(request):
	user = User.objects.get(emailId=str(request.session['email']))
	posts = user.post_set.all()
	postsrep = []
	frreq = user.receiver.filter(friend=False)
	frnds = user.receiver.filter(friend=True)
	frnds.append(user.sender.filter(friend=True))
	for post in posts:
		postsrep.append({'post':post,'replies':post.reply_set.all()})
	context = {
		'user':user,
		'posts':postsrep,
		'frnds':frnds,
		'frreq':frreq,
	}
	return render(request,'post/hello.html',context)
def post(request):
	text=request.POST['post']
	user = User.objects.get(emailId=str(request.session['email']))
	u=Post(text=text,user=user)
	u.save()
	return redirect('/wall/')
def reply(request):
	text = request.POST['reply']
	user = User.objects.get(emailId=str(request.session['email']))

	

