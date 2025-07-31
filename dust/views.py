from django.shortcuts import render
from .models import Post

def shoplist(request):
    #db에서 query select * from post
    posts = Post.objects.all()
    return render(request,
                  template_name='shop/shoplist.html',
                  context={'posts':posts})


def shopdetail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,
                  'shop/shopdetail.html',
                  context={'post':post})

