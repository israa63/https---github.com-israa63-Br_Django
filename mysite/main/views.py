from multiprocessing import context
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render
from .models import Post
from .models import Category

def index(request):
   # return HttpResponse("Hello, world")
   main= Category.objects.all()
   context={"main":main}
   #output =','.join([p.titel for p in main])
   #blogcontents=','.join([p.content for p in main])
  # context={'titles':output, 'bcontent':blogcontents}
   #return HttpResponse(output)
   return render(request,'main/main.html',context)

def getPost(request,main_id):
    post =Post.objects.get(id=main_id)
    context ={"post":post}
    return render(request,'main/mains.html',context=context)

def getCategory(request,Category_id):
    category =Category.objects.get(id=Category_id)
    context ={"post":category}
    return render(request,'main/mains.html',context=context)







  

'''''
def getPost(request,main_id):
    post = Post.objects.get(pk=main_id)
  
    context = {'post':Post}
    return render(request,'main/mains.html',context)
'''''




