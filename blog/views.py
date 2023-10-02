# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.http import JsonResponse

@login_required
def post_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blog:post_list')  # Redirect to the list of blog posts after posting
    else:
        form = PostForm()

    return render(request, 'blog/post_blog.html', {'form': form})

def post_list(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 6)  # Show 6 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()

    # Count the number of likes and favorites
    likes_count = post.likes.count()
    favorites_count = post.favorites.count()

    # Handle adding comments
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            
            comments = post.comments.all()
            return redirect('blog:post_detail', pk=pk)
            
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {
        'post': post,
        'comments': comments,
        'is_liked': is_liked,
        'comment_form': comment_form,
        'likes_count': likes_count,
        'favorites_count': favorites_count,
    }
    return render(request, 'blog/post_detail.html', context)

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('blog:post_detail', pk=pk)

def favorite_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.favorites.filter(id=request.user.id).exists():
        post.favorites.remove(request.user)
    else:
        post.favorites.add(request.user)
    return redirect('blog:post_detail', pk=pk)

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the user is the author or a superuser
    if request.user == post.author or request.user.is_superuser:
        if request.method == 'POST':
            # Include request.FILES to handle file uploads
            post_form = PostForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                post_form.save()
                messages.success(request, 'Post updated successfully.')
                return redirect('blog:post_detail', pk=post.pk)
        else:
            # Display the form for updating the post
            post_form = PostForm(instance=post)
        
        return render(request, 'blog/update_post.html', {'post_form': post_form, 'post': post})

    # If the user is not authorized to update, show an error message
    messages.error(request, 'You do not have permission to update this post.')
    return redirect('blog:post_detail', pk=post.pk)

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the user is the author or a superuser
    if request.user == post.author or request.user.is_superuser:
        if request.method == 'POST':
            # Delete the post
            post.delete()
            messages.success(request, 'Post deleted successfully.')
            return redirect('blog:post_list')

        return render(request, 'blog/delete_post.html', {'post': post})

    # If the user is not authorized to delete, show an error message
    messages.error(request, 'You do not have permission to delete this post.')
    return redirect('blog:post_detail', pk=post.pk)


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()

            if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                # If it's an AJAX request, return a JSON response
                return JsonResponse({'success': True})
            else:
                # If it's a normal form submission, redirect to the post detail page
                return redirect('blog:post_detail', pk=pk)
        else:
            if request.is_ajax():
                # If it's an AJAX request and the form is invalid, return a JSON response with errors
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html', {'form': form})

