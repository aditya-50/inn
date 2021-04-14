from django import template
from insta.models import CustomUser,Post,Comment,likes,Hashtag
register=template.Library()
import datetime
# def ch(value,arg):
#     if value.sender==arg:
#         return value.reciever
#     else:
#         return value.sender


def mod(value):

    if int(value-1)%3==0 and value>=3:

        return True
def next(value):
    return value.upper()


def lis(value,arg):
    arg=int(arg)-1
    return value[arg]

def li(value,arg):
    arg=int(arg)-1
    return len(value[arg])

def check(value):
    if value==None:

        return False
    return value

def tr(value):
    arr=[]
    brr=[]
    fol=value.followers.all()

    
    a=list(likes.objects.filter(post__author=value))
    b=list(Comment.objects.filter(post__author=value))
    a.extend(b)

    def l(val):
        if "time" in val.__dict__.keys():
            return val.time
        else:
            return val.comment_published_date
    a=sorted(a,key=lambda x:l(x),reverse=True)
    a.extend(fol)
    return a
    # return value

def indi(value,arg):
    return value
    # if int(arg)==1:
    #     return value[int(arg)].picture.url
    # return value[int(arg)]

def dat(value):

    try:
        v=value.time
    except:
        v=value.comment_published_date
    finally:
        t=datetime.datetime.now(v.tzinfo)
        final=t-v
        if int(final.days)==0:
            return "Today"
        else:
            return f"{final.days}d ago"

    #
    # if "time" in value.__dict__:
    #     v=value.time
    # else:
    #     v=value.comment_published_date

def si(value):
    return value*(70/100)

def chat(value,arg):
    for u in value:
        if u != arg:
            print(u)
            print("%"*1000)
            return u.display_picture.url
def cha(value,arg):
    for u in value:
        if u != arg:
            return u

def hh(value,arg):
    for u in value.user.all():
        if u != arg:
            return u.pk

def v(value):
    if len(value)>13:
        return value[:15]+" ...."
    return value


def count(value):
    return len(value)



def c(value,arg):
    if value and arg:
        if int(value)==int(arg):
            return True
    return False

def spliter(value):
    return value.split()
def hasher(value):    
    a=Hashtag.objects.get(page=value)
    return a.pk
def chg(value):
    return "#" in value

def len_check(value):
    if len(value)>=38:
        return True

register.filter('si',si)
register.filter('indi',indi)
register.filter('try',tr)
register.filter('check',check)
register.filter('next',next)
register.filter('mod',mod)
register.filter('lis',lis)
register.filter('li',li)
register.filter('dat',dat)
register.filter('chat',chat)
register.filter('cha',cha)
register.filter("hh",hh)
register.filter("v",v)
register.filter("count",count)
register.filter("c",c)
register.filter("hasher",hasher)
register.filter("split",spliter)
register.filter("chg",chg)
register.filter("length",len_check)