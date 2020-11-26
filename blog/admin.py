from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','auther','body','publish','created','update','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','auther','created','publish',)
    search_fields=('title','body',)
    raw_id_fields=('auther',)
admin.site.register(Post,PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','created','updated','active']

    list_filter=('active','created','updated',)
    search_fields=('name','email','body',)
admin.site.register(Comment,CommentAdmin)
