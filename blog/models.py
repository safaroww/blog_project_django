from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.admin import display
from django.utils.html import format_html
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Basliq')
    description = models.TextField(null=True, blank=True, verbose_name='Aciqlama')
    content = models.TextField()
    show = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    view_count = models.IntegerField(default=0)
    main_image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"pk": self.pk})
    
    @display(description='Movcud Esas Sekil')
    def main_image_tag(self):
        return format_html(f'<img width="200" src="{self.main_image.url}">')
    
    class Meta:
        verbose_name = 'Meqale'
        verbose_name_plural = 'Meqaleler'

# orm

class ArticleImage(models.Model):
    # article = models.ForeignKey('blog:article', on_delete=models.CASCADE)
    # article = models.ForeignKey('article', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='article-images/') 

    @display(description='Movcud Sekil')
    def current_image(self):
        return format_html(f'<img width="200" src="{self.image.url}">')
    

class ArticleReview(models.Model):
    star_count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews')

# article.articlerewiev_set
# article.reviews