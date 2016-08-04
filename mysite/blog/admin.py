from django.contrib import admin
from .models import Post, Comment
from pagedown.widgets import AdminPagedownWidget
from django import forms
# Register your models here.

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())
    class Meta:        
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', '-publish']
    list_per_page = 5
    form = PostForm

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
