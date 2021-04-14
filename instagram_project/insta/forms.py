from django import forms

from .models import Comment,Register,CustomUser,Chats,Post

class RegisterForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=CustomUser
        fields=('email','full_name','user_name','password','display_picture')
class CommentForm(forms.ModelForm):
    class Meta:
        
        model=Comment
        fields=('text',)
        labels = {"text":""}
        widgets = {'text':forms.TextInput(attrs={'placeholder':'Add a Comment...'})}
        work_or_study=forms.CharField(label="Bio", widget=forms.TextInput(attrs={'label':'','placeholder':'something interesting about you'}))

class ChatForm(forms.ModelForm):
    class Meta:
        model=Chats
        fields=('text',)
        labels = {"text":""}
        widgets = {'text':forms.TextInput(attrs={'placeholder':'Message...'})}

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("picture","text","tag",)
