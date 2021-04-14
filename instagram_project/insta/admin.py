from django.contrib import admin
from .models import CustomUser,Comment,Post,likes,Chats,Hashtag,Story
# Register your models here.
admin.site.register(Chats)
admin.site.register(Comment)
admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(likes)
admin.site.register(Hashtag)
admin.site.register(Story)