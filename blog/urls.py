from django.urls import path
from .views import blog, blogdetail, add_article, edit_article, delete_article

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('blog/<int:pk>/', blogdetail, name='blog-detail'),
    path('add-article/', add_article, name='add-article'),
    path('edit-article/<int:pk>/', edit_article, name='edit-article'),
    path('delete-article/<int:pk>/', delete_article, name='delete-article'),
]
