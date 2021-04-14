

# Create your models here.
from django.db import models
from django.shortcuts import reverse
from datetime import datetime
from instagram_project import settings
from django.contrib.auth.models import User,AbstractBaseUser,PermissionsMixin,BaseUserManager
# from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
from django.utils import timezone

# print(timezone.tzinfo)
def user_directory_path(instance, filename):
    print(instance)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # print('user_{0}/{1}'.format(instance.id, filename))
    return 'dp/user_{0}/{1}'.format(instance.id, filename)

def user_directory(instance, filename):
    # print(instance)
    return 'posts/user_{0}/{1}'.format(instance.author, filename)


class CustomAccountManager(BaseUserManager):
    def create_user(self,email,user_name,full_name,password,**other_fields):
        email=self.normalize_email(email)
        user=self.model(email=email,user_name=user_name,full_name=full_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,user_name,full_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Super user must be assigned to is_staff=True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Super user must be assigned to is_superuser=True'
                    )
        return self.create_user(email, user_name, full_name, password, **other_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    user_name=models.CharField(max_length=150,unique=True)
    full_name=models.CharField(max_length=150)
    start_date=models.DateTimeField(default=timezone.now)
    about=models.TextField(blank=True)
    # last_follow=models.ForeignKey('self',related_name='last',blank=True,null=True,on_delete=models.CASCADE)
    Private=models.BooleanField(default=False)
    saved=models.ManyToManyField('Post',blank=True,null=True,symmetrical=False,related_name='saved')
    is_staff=models.BooleanField(default=False)
    online=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    followers=models.ManyToManyField('self',blank=True,null=True,symmetrical=False,related_name='follower')
    following=models.ManyToManyField('self',blank=True,null=True,symmetrical=False,related_name='f')
    posts=models.IntegerField(default=0)
    birth_date = models.DateField(blank=True, null=True)
    display_picture=models.ImageField(upload_to=user_directory_path)
    objects=CustomAccountManager()

    USERNAME_FIELD='user_name'
    REQUIRED_FIELDS=['full_name','email']

    def __str__(self):
        return self.user_name


    def get_absolute_url(self):
        return reverse('insta:home_page')

class Hashtag(models.Model):
    page=models.CharField(max_length=10000)
    start_date=models.DateTimeField(default=timezone.now)
    # followers=models.ManyToManyField(CustomUser,blank=True,null=True,symmetrical=False,related_name='hash_follower')
    posts=models.ManyToManyField('Post',blank=True,null=True,symmetrical=False,related_name="posts")
    
    def get_absolute_url(self):
        return reverse('insta:home_page')

class Post(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to=user_directory)
    time=models.DateTimeField(auto_now_add=True)
    text=models.TextField(max_length=5000,default='')
    tag=models.ManyToManyField(CustomUser,blank=True,null=True,related_name="Tag")

    # published_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        st=""
        for n in self.text.split():
            if "@" in n or "#" in n:
                continue
            else:
                st+=n+" "
        return f"{self.author} {st}"


class Comment(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_published_date=models.DateTimeField(auto_now_add=True)
    approve_comment=models.BooleanField(default=True)
    text=models.TextField(max_length=3000,default="")



    def __str__(self):
        return self.text

    def remove(self):
        self.approve_comment=False
        self.save()
# CustomUser.objects.get(user_name='#Umang')


class Register(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user_name

class likes(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Chats(models.Model):
    user=models.ManyToManyField(CustomUser,symmetrical=False,related_name='user',null=True,blank=True)
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sender')
    reciever=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='reciever')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post',null=True,blank=True)
    time=models.DateTimeField(auto_now_add=True)
    text=models.CharField(max_length=10000000,default="")

class Story(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to=user_directory)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user_name