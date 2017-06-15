from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Post,Reply,User
# Create your views here.
def wall(request):
	user = User.objects.get(emailId=str(request.session['email']))
	posts = user.post_set.all()
	postsrep = []
	for post in posts:
		postsrep.append({'post':post,'replies':post.reply_set.all()})
	context = {
		'user':user,
		'posts':postsrep
	}
	return render(request,'post/hello.html',context)
