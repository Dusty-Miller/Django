from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,CommentForm
from .models import Post, Category ,Comment



#CBV
class PostList(ListView):
    model = Post
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'



def index(request):
    #db에서 query select * from post
    posts = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request,
                  template_name='blog/index.html',
                  context={'posts':posts,
                           'categories':categories})

def category(request, slug):
    categories = Category.objects.all()
    if slug == 'no_category':
        #미분류인 경우
        post = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post = Post.objects.filter(category=category)
    return render(request,
            template_name='blog/index.html',
            context={'posts': post,
                           'categories': categories})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments= Comment.objects.filter(post=post)
    categories = Category.objects.all()
    commentform = CommentForm()
    return render(request,
                  'blog/detail.html',
                  context={'post':post,
                  'categories':categories,
                           'comments':comments,
                           'commentform':commentform})

def create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        #작성하다가 제출 버튼을 누른 경우
        postform = PostForm(request.POST,request.FILES)
        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.title = post1.title + ""
            postform.save()
            return redirect('/blog/')
    else: #get
        postform = PostForm()
    return render(request,
                  template_name="blog/postform.html",
                  context={'postform':postform,
                  'categories':categories})

def createfake(request):
    post = Post()
    post.title = "새싹 용산구"
    post.content='나진상가 3층'
    post.save()
    return redirect('/blog/')

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('/blog/')
        else:
            postform = PostForm(instance=post)
    else:
        postform=PostForm(instance=post)

    return render(request,
                  template_name="blog/postupdateform.html",
                  context={'postform':postform,})


def createcomment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
    # 제출
        commentform = CommentForm(request.POST, request.FILES)
        if commentform.is_valid():
            comment1 = commentform.save(commit=False)
            comment1.post = post
            comment1.save()
            return redirect(f'/blog/{post.pk}/')

    else:
        commentform = CommentForm()

    return render(request, template_name='blog/commentform.html', context={'commentform': commentform})


def updatecomment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        commentform = CommentForm(request.POST, request.FILES, instance=comment)
        if commentform.is_valid():
            commentform.save()
            return redirect(f'/blog/{comment.post.pk}/')
    else:
        commentform = CommentForm(instance=comment)
    return render(request, template_name="blog/comment_update_form.html", context={'commentform': commentform})


def deletecomment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/')















