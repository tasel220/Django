from django.shortcuts import render, redirect
from .models import Post, Comment, Like

from django.contrib.auth.models import User

from tags.models import Tag


# Create your views here.
def index(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        tags = Tag.objects.all()
        return render(
            request,
             'blogPosts/index.html',
            {
                'posts': posts,
                'tags':tags
            }
        )
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(title=title, content=content, author=request.user)
        post.tags.set(request.POST.getlist('tags'))
        return redirect('blogPosts:index')

def new(request):
    tags = Tag.objects.all()
    return render(request, 'blogPosts./new.html')

def show(request, id):
    post = Post.objects.get(id=id)
    tags = Tag.objects.filter(posts=post)
    return render(request, 'blogPosts/show.html', {'post':post})

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete() # 선택된 모델 인스턴스를 삭제하는 query 함수입니다.
    return redirect('blogPosts:index')

def update(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        tags = Tag.objects.all()
        return render(request, 'blogPosts/update.html', {'post': post, 'tags': tags})
    elif request.method == 'POST':
        post = Post.objects.filter(id=id)
        post.update(title=request.POST['title'], content=request.POST['content'])
        post.first().tags.set(request.POST.getlist('tags'))
        return redirect('blogPosts:show', id=id)


class CommentView:
    def create(request, id):
        content = request.POST['content']
        Comment.objects.create(post_id=id, content=content, author=request.user)
        return redirect('/posts')
    def delete(request, id, cid):
        comment = Comment.objects.get(id=cid)
        comment.delete()
        return redirect(f'/posts/{id}')

class LikeView:
    def create(request, id):
        post = Post.objects.get(id=id)
        like_list = post.like_set.filter(user_id=request.user.id)
        if like_list.count() > 0:
            post.like_set.get(user=request.user).delete()
        else:
            Like.objects.create(user=request.user, post=post)
        return redirect ('/posts')            

