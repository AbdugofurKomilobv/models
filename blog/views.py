from django.shortcuts import redirect, render
from .models import *

def home_page(request):

    category = Category.objects.all()
    posts = Post.objects.all()
    db = {
        "category":category,
        "posts":posts,
    }
  

    return render(request=request,template_name='index.html',context=db)



def batafsi(request,post_id):
    post = Post.objects.get(id=post_id)
    category = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")


        if all([name,comment]): 
            Comments.objects.create(
                author = name,
                comment = comment,
                post = post
            )
        return redirect('home')
     

    return render(request,'batafsil.html',context={'post':post,'category':category})