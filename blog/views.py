from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm, EmailPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
# Create your views here.

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    form = PostForm()
    if request.POST:
        post = PostForm(request.POST)
        post.save()
    return render(request,'blog/index.html',{'posts':posts, "form":form})

def create(request):
    context={}
    template_name=''
    return render(request,template_name,context)

def show(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    return render(request,'blog/show.html',{"post":post})

def update(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    context={"post":post}
    template_name=''
    return render(request,template_name,context)

def delete(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    
    template_name=''
    return render(request,'blog/index.html',{"post":post})

def share(request, uuid):
    # Retrieve post by id
    post = get_object_or_404(
        Post,
        uuid=uuid,
        status=Post.Status.PUBLISHED
    )
    form = EmailPostForm()
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = (
                f"{cd['name']} ({cd['email']})" 
                f"recommends you read {post.title}"
            )
            message = ( 
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}\'s comments: {['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            sent = True
            # ... send email
        else:
            form = EmailPostForm()
    return render(request,'blog/share.html', {'post': post, 'form': form, 'sent': sent })
