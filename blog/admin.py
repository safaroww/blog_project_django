from django.contrib import admin
from .models import Article, Author, Tag, ArticleImage

# Register your models here.

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(ArticleImage)



@admin.action(description='Make visible')
def make_visible(modeladmin, request, queryset):
    queryset.update(show=True)

@admin.action(description='Make invisible')
def make_invisible(modeladmin, request, queryset):
    queryset.update(show=False)


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 0
    readonly_fields = ['current_image']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'content', 'show', 'tags', 'main_image', 'author', 'view_count', 'created']
    # exclude = ['view_count']
    fieldsets = (
        ('Text Fields', {
            "fields": (
                'title', 'description', 'content'
            ),
            'classes': ('collapse',)
        }),
        ('Features', {
            "fields": (
                'show', 'tags', 'view_count', 'main_image_tag', 'main_image', 'author'
            ),
        })
    )
    
    readonly_fields = ['view_count', 'created', 'main_image_tag']
    list_display = ['title', 'show', 'view_count', 'author', 'created']
    list_filter = ['tags', 'author', 'created']
    search_fields = ['title', 'author__user__first_name', 'tags__title']
    actions = [make_visible, make_invisible]
    inlines = [ArticleImageInline]