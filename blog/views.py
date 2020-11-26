from blog.forms import CommentForm
from django.core.paginator import Paginator

from blog.models import Post,Comment
from django.shortcuts import render,get_object_or_404
from taggit.models import Tag
# Create your views here.
def blog_list(request,tag_slug=None):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    post_list=paginator.get_page(page_number)
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])

    return render(request,'blog/post_list.html',{"post_list":post_list,'tag':tag})

from django.db.models import Count
def blog_details(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)
    #comments = post.comment_set.all()
    post_tags_ids=post.tags.values_list('id',flat=True)
    similiar_post=Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similiar_post=similiar_post.annotate(same_tags=Count('tags')).order_by('-same_tags','publish')[:4]
    comments=post.comments.filter(active=True)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
        else:
            form=CommentForm()
    return render(request,"blog/detail.html",{'post':post,'form':form,'comments':comments,'csubmit':csubmit,'similiar_post':similiar_post})
