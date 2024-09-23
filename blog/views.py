from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm, EmailPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    """
    This function handles the display of the blog's index page.
    It retrieves all published posts, paginates them, and renders the index.html template with the posts and a form for creating new posts.

    Parameters:
    - request: The Django request object containing information about the current request.

    Returns:
    - A Django render response object containing the index page with the paginated posts and a form for creating new posts.
    """
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
    return render(request,'blog/posts/index.html',{'posts':posts, "form":form})

def create_post(request):
    form = PostForm()
    return render(request,'blog/posts/create.html',{"form":form})

def show_post(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    return render(request,'blog/posts/show.html',{"post":post})

def update_post(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    context={"post":post}
    template_name=''
    return render(request,template_name,context)

def delete_post(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    
    template_name=''
    return render(request,'blog/posts/index.html',{"post":post})

def share_post(request, uuid):
    """
    This function handles the sharing of a blog post via email.
    It retrieves a published post by its UUID, processes a form for email submission,
    and sends an email with the post's details and user comments.

    Parameters:
    - request: The Django request object containing information about the current request.
    - uuid: The UUID of the blog post to be shared.

    Returns:
    - A Django render response object containing the shared post, form, and a boolean indicating whether the email was sent.
    """
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
    return render(request,'blog/posts/share.html', {'post': post, 'form': form, 'sent': sent })


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(request, 'blog/post/comment.html', { 'post': post, 'form': form, 'comment': comment })
