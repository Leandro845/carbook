from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from .form import CommentForm
from django.core.paginator import Paginator
from django.db.models import Count

def blog(request):
    # Fetch all blog posts and order them by the latest first.
    posts = Blog.objects.all().order_by('-id')

    # Paginate the posts, 6 per page.
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    obj_list = paginator.get_page(page)

    # Render the blog list page with the paginated posts.
    return render(request, 'blog.html', {'obj_list': obj_list})

def blogs_per_brand(request, brand_id):
    # Filter blog posts by the selected car brand and order them by the latest first.
    blogs = Blog.objects.filter(car_brand__id=brand_id).order_by('-id')

    # Paginate the filtered blogs, 6 per page.
    paginator = Paginator(blogs, 6)
    page = request.GET.get('page')
    obj_list = paginator.get_page(page)

    # Render the blog list page for the selected brand.
    return render(request, 'blogs_per_brand.html', {'obj_list': obj_list})

def blog_detail(request, blog_id):
    # Get the specific blog post or return a 404 error if not found.
    post = get_object_or_404(Blog, pk=blog_id)

    # Get the count of blog posts by each car brand.
    posts_by_brand = Blog.objects.values('car_brand__name', 'car_brand').annotate(total=Count('car_brand'))

    # Fetch 3 related blog posts excluding the current one.
    blogs = Blog.objects.exclude(id=post.id).order_by('-id')[:3]
    
    # Create a new comment form.
    comment_form = CommentForm()

    # Fetch comments related to the post, filtering by top-level comments.
    comments = Comment.objects.filter(blog=post, parent__isnull=True).order_by('-created')

    # Prepare context variables for rendering the blog detail page.
    vars = {
        'post': post,
        'posts_by_brand': posts_by_brand,
        'blogs': blogs,
        'comment_form': comment_form,
        'comments': comments,
    }
    
    # Render the blog detail page.
    return render(request, 'blog-single.html', vars)

def post_comment(request, blog_id):
    # Get the specific blog post or return a 404 error if not found.
    post = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        # Get comment details from the POST request.
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('content')
        parent = request.POST.get('parent_id')

        # Check if the comment is a reply to another comment.
        if parent:
            parent_obj = Comment.objects.get(id=parent)
        else:
            parent_obj = None

        # Create and save a new comment.
        create_comment = Comment(
            blog=post,
            name_user=name,
            email=email,
            body=body,
            parent=parent_obj
        )
        create_comment.save()

    # Redirect back to the blog detail page after saving the comment.
    return redirect('blog_detail', blog_id=post.id)
