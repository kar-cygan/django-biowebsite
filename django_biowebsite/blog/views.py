from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Category, Author, Post
from .forms import CategoryForm

def blog_view(request, category_name=None, author_name=None):
    if category_name:
        queryset = Post.objects.filter(category__name=category_name)
    elif author_name:
        queryset = Post.objects.filter(author__name=author_name)
    else:
        queryset = Post.objects.all()
    
    queryset = queryset.filter(public=True).order_by('-date_create')
    paginator = Paginator(queryset, 2) # 2 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': Category.objects.all(),
        'category_name': category_name,
        'page_obj': page_obj,
        'n_posts': queryset.count(),
    }
    return render(request, 'blog/blog.html', context)

def post_view(request, post_id):
    context = {
        'post_object': get_object_or_404(Post, id=post_id),
        'categories': Category.objects.all(),
        'category_name': None,
    }
    return render(request, 'blog/post.html', context)

@login_required()
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog category has been created.')
            return redirect('blog:blog_view')
    else:
        form = CategoryForm()
    return render(request, 'blog/category_create.html', {'form': form})

@login_required()
def category_edit_view(request, category_name):
    category_obj = get_object_or_404(Category, name=category_name)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog category has been updated.')
            return redirect('blog:blog_view')
    else:
        form = CategoryForm(instance=category_obj)
    return render(request, 'blog/category_create.html', {'form': form})
