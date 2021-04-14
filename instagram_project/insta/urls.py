# login,signup,home_page
from . import views

from django.urls import path
from django.conf.urls import url
app_name='insta'

urlpatterns=[
    path('user_/',views.HomePageView.as_view(),name='home_page'),
    path('explore/',views.Explore.as_view(),name='explore'),
    path('user/profile/<int:pk>/',views.UserProfile.as_view(),name='user_profile'),
    path('follow/<int:pk>/',views.follow,name='follow'),
    path('unfollow/<int:pk>/',views.unfollow,name='unfollow'),
    path('unlike/<int:pk>/',views.unlike,name='unlike'),
    path('like/<int:pk>/',views.like,name='like'),
    path('save/<int:pk>/',views.saved,name='save'),
    path('unsave/<int:pk>/',views.unsaved,name='unsave'),
    path('post/<int:pk>/detail',views.PostDetail.as_view(),name='detail'),
    path('user/saved/<int:pk>/',views.Saved.as_view(),name='saver'),
    path('user/inbox',views.Inbox.as_view(),name='inbox'),
    path('user/inbox/<int:pk>/',views.ChatsDetail.as_view(),name="chater"),
    path("user/inbox/<int:pk>/<str:username>",views.post_chat,name="post_chat"),
    path("user/new/post",views.post_form,name="new_post"),
    path("user/Hashtag/<int:pk>/",views.HashTagPage.as_view(),name="hash"),
    path('user_/story/<int:pk>/',views.StoryDetail.as_view(),name='story'),




]
