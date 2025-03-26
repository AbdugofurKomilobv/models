from django.shortcuts import redirect, render
from .models import *

from .utils import korishlar_soni

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

    request.session.modified = True  # Sessiyani yangilash

    if post.id not in korishlar_soni(request):
     korishlar_soni(request).append(post.id)  # ID-ni sessiyaga qo‘shish
     request.session.save()  # Sessiya o‘zgarishini saqlash
     post.views += 1  # Ko‘rishlar sonini oshirish
     post.save()  # O‘zgarishlarni bazaga yozish



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