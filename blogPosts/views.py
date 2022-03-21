from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'blogPosts/index.html', {'posts': posts})
    elif request.method == 'POST':  
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('blogPosts:index')

def new(request):
    return render(request, 'blogPosts./new.html')

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blogPosts/show.html', {'post':post})

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete() # 선택된 모델 인스턴스를 삭제하는 query 함수입니다.
    return redirect('blogPosts:index')
