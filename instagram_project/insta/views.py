from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import reverse
from .forms import (RegisterForm,CommentForm,ChatForm,PostForm)
from .models import CustomUser,Post,Comment,likes,Chats,Hashtag,Story
from random import shuffle
from django.views.generic import (ListView,DetailView,DeleteView,CreateView)
# Create your views here.
from django.contrib.auth import login,logout,authenticate
from collections import Counter
from django.shortcuts import get_object_or_404
import datetime
import json
def register_view(request):
    registered=False
    if request.method=='POST':
        print(request.FILES)
        user=RegisterForm(request.POST,request.FILES)
        if user.is_valid():
            user=user.save()
            user.set_password(user.password)
            user=user.save()
            register=True
            password=request.POST['password']
            username=request.POST['user_name']
            user=authenticate(username=username,password=password)
            print(user)
            if user:
                print("hogaya")
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('insta:home_page'))
                else:
                    return HttpResponse('Account not active')
            else:
                print("nhihua")
                print(user,"yaar signup")
                return HttpResponseRedirect(reverse('signup'))
    else:
        user=RegisterForm()
    return render(request,'insta/register/signup.html',{'form':user})


def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                print("hello you have logged in ")
                user.online=True
                user.save()
                login(request,user)
                return HttpResponseRedirect(reverse('insta:home_page'))
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponseRedirect(reverse('signup'))
    else:
        return render(request,'insta/register/login.html')


@login_required
def user_logout(request):
    print("you have logged")
    request.user.online=False
    request.user.save()
    print(request.user.online,"online or ofline"*100)
    logout(request)
    return HttpResponseRedirect(reverse('login'))

class Saved(DetailView):
    model=CustomUser
    template_name='insta/main/saved.html'
    context_object_name='user_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['User']=CustomUser.objects.get(user_name=context['object'])
        po=CustomUser.objects.get(user_name=context['object']).saved.all()
        context['p']=len(po)
        context['posts']=po.order_by('-time')

        return context


class HomePageView(ListView):
    # model=Post
    template_name='insta/main/home.html'
    # context_object_name='hell'
    model=Post
    form_class=CommentForm
    def get_success_url(self):
        return reverse('explore')


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        a=CustomUser.objects.all()
        context['Users_all']=a
        trr=[]
        query = self.request.GET.get('chat')
        we=self.request.GET.get("hide")


        if query:
            for user in a:
                if user.user_name.lower()==query.lower() or query.lower()==user.full_name.lower():
                    trr.append(user)
                    continue

                try:
                    a=user.user_name.lower().index(query.lower())
                except:
                    pass
                else:
                    if a==0:
                        trr.append(user)
                        continue

                try:
                    b=user.full_name.lower().index(query.lower())
                except:
                    pass
                else:
                    if b==0:
                        trr.append(user)
                        continue
        context['chat_user']=trr
        context['post_pk']=we
        trr=[]
        query = self.request.GET.get('search')
        if query:
            for user in Hashtag.objects.all():
                try:
                    c=query.lower()==user.page.lower() or user.page.lower().index(query.lower())==0
                except:
                    pass
                else:
                    if c:
                        trr.append(user)
                        continue
            for user in a:
                if user.user_name.lower()==query.lower() or query.lower()==user.full_name.lower():
                    trr.append(user)
                    continue

                try:
                    a=user.user_name.lower().index(query.lower())
                except:
                    pass
                else:
                    if a==0:
                        trr.append(user)
                        continue

                try:
                    b=user.full_name.lower().index(query.lower())
                except:
                    pass
                else:
                    if b==0:
                        trr.append(user)
                        continue
        context['search']=trr
       #    postresult = Article.objects.filter(title__contains=query)
       #    result = postresult
       # else:
       #     result = None
       # return result

        context['form']=CommentForm(initial={'author':self.request.user})
        following=list(CustomUser.objects.get(user_name=self.request.user).following.all())
        story=[]
        following.append(self.request.user)
        for f in Story.objects.all():
            if f.author in list(following):
                story.append(f)
        context['story']=story 
        u=CustomUser.objects.get(user_name=self.request.user)
        # comments=Comment.objects.filter(post=)
        brr=[]
        for f in following:
            brr.extend(list(f.following.all()))
        # print(brr)
        l=[]
        a=Counter(brr)
        mutual=[]
        for key,value in a.items():
            if self.request.user==key or key in self.request.user.following.all():
                continue
            if value>=1:
                mutual.append(value)
                l.append(key)
        timezone = CustomUser.objects.get(pk=3).start_date.tzinfo
        context['mutual']=mutual


        tod = datetime.datetime.now(timezone)
        d = datetime.timedelta(days = 15)
        a = tod - d     
        ll=[]
        # print(a)
        # print( CustomUser.objects.get(pk=3).start)
        # print()
        b=[]
# Current datetime for the timezone of your variable
        z=False
        for users in CustomUser.objects.all():
            if users not in CustomUser.objects.get(user_name=self.request.user).following.all():
                    if users.start_date>a or users not in l:
                        b.append(users)

        context['b']=ll
        context['suggest']=l
        arr=[]
        followers=list(CustomUser.objects.get(user_name=self.request.user).following.all())
        followers.append(self.request.user)

        print(followers,self.request.user)
                # themes.sort(key=lambda t: pks_list.index(t.pk))

        for follower in followers:
            if follower==self.request.user:
                print(follower,"yes")
            try:
                a=Post.objects.filter(author=follower)
            except:
                pass
            else:
                # a=Post.objects.get(author=follower)
                arr.extend(a)

        arr.sort(key=lambda x:x.time,reverse=True)
        l=[]
        crr=[]
        for post in arr:
            try:
                a=likes.objects.get(post=post,user=self.request.user)
            except:
                crr.append(False)
            else:
                crr.append(True)
            l.append(Comment.objects.filter(post=post).order_by("-comment_published_date"))
        context['comments']=l
        context['hell']=arr
        context['likes']=crr
        return context


    def post(self,request,*args,**kwargs):
        form=CommentForm(request.POST)
        if form.is_valid():
            form=CommentForm(request.POST)
            form=form.save(commit=False)
            form.author=self.request.user
            # print(self.kwargs.get('parameter'))
            form.post=get_object_or_404(Post,pk=int(request.POST['hidden']))
            # print(form)
            form.save()
            return HttpResponseRedirect(reverse('insta:home_page'))

            # return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse('insta:explore'))
            return self.form_invalid(form)

    def form_valid(self,form):
        return super().form_valid(form)
    #
    # def form_invalid(self,form):
    #     return super().form_invalid()



class Explore(ListView):
    # model=Post
    template_name='insta/main/explore.html'
    context_object_name='posts'
    def get_queryset(self):
        posts=list(Post.objects.all())
        shuffle(posts)
        return posts

def UserProfile(request,pk):
    user=get_object_or_404(CustomUser,pk=pk)
    po=Post.objects.filter(author=user)
    p=len(po)
    posts=sorted(po,key=lambda x:x.time,reverse=True)

    return render(request,'insta/main/user.html',{'User':user,'po':po,'p':p})

class UserProfile(DetailView):
    model=CustomUser
    template_name='insta/main/user.html'
    context_object_name='user_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['User']=context['object']
        po=Post.objects.filter(author=context['object'])
        context['p']=len(po)
        context['posts']=sorted(po,key=lambda x:x.time,reverse=True)
        # print("%"*100)

        return context

def follow(request,pk):
    user=CustomUser.objects.get(user_name=request.user)
    last_follow=user
    following=get_object_or_404(CustomUser,pk=pk)
    user.last_follow=following
    user.save()
    user.following.add(following)
    following.followers.add(user)
    return HttpResponseRedirect(reverse('insta:user_profile',args=(pk,)))



def unfollow(request,pk):
    user=CustomUser.objects.get(user_name=request.user)
    following=get_object_or_404(CustomUser,pk=pk)
    print(user.following.all(),"before")
    user.following.remove(following)
    user.save()
    print(user.following.all(),"after")
    print(following.followers.all())

    following.followers.remove(user)
    following.save()
    print(following.followers.all())
    return HttpResponseRedirect(reverse('insta:user_profile',args=(pk,)))
#
#
# def like(request,pk):
#     user=CustomUser.objects.get(user_name=request.user)
#     post=get_object_or_404(Post,pk=pk)
#     post.likes.add(user)
#
#     return HttpResponseRedirect(reverse('insta:home_page'))
#
# def unlike(request,pk):
#     user=CustomUser.objects.get(user_name=request.user)
#     post=get_object_or_404(Post,pk=pk)
#     post.likes.remove(user)

    return HttpResponseRedirect(reverse('insta:home_page'))

def saved(request,pk):
    user=CustomUser.objects.get(user_name=request.user.user_name)
    post=get_object_or_404(Post,pk=pk)
    print(user.saved.all())
    user.saved.add(post)
    print(user.saved.all())
    

    return HttpResponseRedirect(reverse('insta:home_page'))

def unsaved(request,pk):
    user=CustomUser.objects.get(user_name=request.user.user_name)
    post=get_object_or_404(Post,pk=pk)
    user.saved.remove(post)

    return HttpResponseRedirect(reverse('insta:home_page'))


# class Notifications(ListView):
#     model=CustomUser
#     template_name='insta/main/base.html'
#     context_object_name='Users'
#     def get_queryset(self):
#         arr=[]
#         brr=[]
#         posts=Post.objects.filter(author=self.request.user)
#         for post in posts:
#             if post.likes.all():
#                 arr.append([post.likes.all(),post.author])
#
#         print(arr)


def like(request,pk):
    user=get_object_or_404(CustomUser,pk=request.user.pk)
    post=get_object_or_404(Post,pk=pk)
    like=likes(post=post,user=user)
    like=like.save()

    return HttpResponseRedirect(reverse('insta:home_page'))


def unlike(request,pk):
    user=get_object_or_404(CustomUser,pk=request.user.pk)
    post=get_object_or_404(Post,pk=pk)
    like=likes.objects.get(user=user,post=post)
    like.delete()

    return HttpResponseRedirect(reverse('insta:home_page'))


class PostDetail(DetailView):
    model=Post
    template_name='insta/main/post_detail.html'
    context_object_name='detail'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['comments']=Comment.objects.filter(post=self.object)
        li=likes.objects.filter(post=self.object)
        for l in li:
            if l.user==self.request.user:
                context['likes']=True
                break
        else:
            context['likes']=False
        return context

class UserList(ListView):
    model=CustomUser
    template_name='insta/main/base.html'
    context_object_name='Users'

class Inbox(ListView):
    model=Chats
    template_name="insta/main/inbox.html"
    context_object_name="Inbox"
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)







        query = self.request.GET.get('search')
        a=CustomUser.objects.all()
        trr=[]
        if query:
            for user in a:
                if user.user_name.lower()==query.lower() or query.lower()==user.full_name.lower():
                    trr.append(user)
                    continue

                try:
                    a=user.user_name.lower().index(query.lower())
                except:
                    pass
                else:
                    if a==0:
                        trr.append(user)
                        continue

                try:
                    b=user.full_name.lower().index(query.lower())
                except:
                    pass
                else:
                    if b==0:
                        trr.append(user)
                        continue
        context['search']=trr

        return context
    def get_queryset(self):
        a=Chats.objects.all()
        tl=[]
        for ch in a:
            if self.request.user in ch.user.all():
                tl.append(ch)
        # print(tl)
        tl=sorted(tl,key=lambda x:x.time,reverse=True)
        ad=[]
        # print(tl)
        # print("%"*100)
        ll=0
        yy=0
        jd=[]
        for c in tl:
            yy+=1
            if sorted(c.user.all(),key=lambda x:x.user_name) not in ad:
                ad.append(sorted(c.user.all(),key=lambda x:x.user_name))
                jd.append(c)
                ll+=1
            else:
                pass
        return jd

class ChatsDetail(DetailView):
    model=CustomUser
    context_object_name="main"
    template_name="insta/main/chat_detail.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        a=Chats.objects.all()
        l=[]
        lr=[]
        lll=CustomUser.objects.get(user_name=context['object'])
        vc=[CustomUser.objects.get(user_name=self.request.user.user_name)]
        vc.append(lll)
        g=False
        for chat in a:
            if context['object'] in chat.user.all() and self.request.user in chat.user.all():
                    g=True
            if sorted(chat.user.all(),key=lambda x:x.user_name) == sorted(vc,key=lambda x:x.user_name):
                l.append(chat)



        context['chats']=l

        a=Chats.objects.all()
        tl=[]
        for ch in a:
            if ch.reciever==self.request.user or ch.sender==self.request.user:
                tl.append(ch)
        # print(tl)
        tl=sorted(tl,key=lambda x:x.time,reverse=True)
        ad=[]

        for c in tl:
            if sorted(c.user.all(),key=lambda x:x.user_name) not in ad:
                lr.append(c)
                ad.append(sorted(c.user.all(),key=lambda x:x.user_name))
            else:
                pass
        # if not g:
        #     lr.append(context['object'])
        context['Inbox']=lr
        context['form']=ChatForm()

        return context

    def post(self,request,*args,**kwargs):
        form=ChatForm(request.POST)
        t=CustomUser.objects.get(pk=self.__dict__['kwargs']['pk'])
        # for u in bg.user.all():
        #
        #     if u!=request.user:
        #         t=u

        a=Chats.objects.all()
        l=[]
        vc=[CustomUser.objects.get(user_name=self.request.user.user_name)]
        vc.append(t)


        if form.is_valid():
            form=ChatForm(request.POST)
            form=form.save(commit=False)
            form.sender=request.user
            form.reciever=t
            form.save()
            form.user.add(request.user)
            form.user.add(t)
            form.save()
            return HttpResponseRedirect(reverse('insta:chater' ,kwargs={'pk':self.__dict__['kwargs']['pk']}))
        else:
            return HttpResponseRedirect(reverse('insta:explore'))

def post_chat(request,pk,username):
    post=get_object_or_404(Post,pk=pk)
    user=get_object_or_404(CustomUser,user_name=username)
    a=Chats()

    a.sender=request.user
    a.reciever=user
    a.post=post
    a.save()
    a.user.add(user)
    a.user.add(request.user)
    a.save()
    return HttpResponseRedirect(reverse("insta:home_page"))


def post_form(request):
    form=PostForm(request.POST,request.FILES)
    # print(,request.FILES,request.GET)
    # print(form)
    # t=CustomUser.objects.get(pk=self.__dict__['kwargs']['pk'])

    # a=Chats.objects.all()
    # l=[]
    # vc=[CustomUser.objects.get(user_name=self.request.user.user_name)]
    # vc.append(t)

    if form.is_valid():
        form=PostForm(request.POST,request.FILES)
        form=form.save(commit=False)
        form.author=request.user
        form.save()
        for pk in request.POST.getlist('tag'):
            a=CustomUser.objects.get(pk=pk)
            form.tag.add(a)
        form.save()
        # print(request.POST['text'].split(),"@"*100)
        for hashtag in request.POST['text'].split():
            if  "#" in hashtag:
                for hash in Hashtag.objects.all():
                    if hash.page==hashtag:
                        hash.posts.add(form)
                        hash.save()
                        break
                else:
                    ha=Hashtag(page=hashtag)
                    ha.save()
                    ha.posts.add(form)
                    ha.save()
        return HttpResponseRedirect(reverse("insta:home_page"))

    return render(request,"insta/main/add_post.html",{"form":form})

class HashTagPage(DetailView):
    model=Hashtag
    template_name="insta/main/hashtag.html"
    context_object_name="User"


class StoryDetail(DetailView):
    model=Story
    context_object_name="Story"
    template_name="insta/main/story_detail.html"
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        stories=Story.objects.all()
        after=[]
        meet=False
        for story in stories:
            if story==context['object']:
                continue
            after.append(story)

            context['after']=after

            # context['total']=[n for n in range((len(after)+1))]
        return context
        


