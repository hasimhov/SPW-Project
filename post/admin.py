from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from post.models import Post,Reply
admin.site.register(Post)
admin.site.register(Reply)