from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('post/<int:post_id>/', views.post_view, name='post_view'),
    path('category/create/', views.category_create_view, name='category_create_view'),
    path('category/<category_name>/', views.blog_view, name='blog_category'),
    path('category/<category_name>/edit/', views.category_edit_view, name='category_edit_view'),
    path('author/<author_name>/', views.blog_view, name='blog_author'),
]
