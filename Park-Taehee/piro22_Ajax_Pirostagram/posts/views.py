from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts, Comment
from .forms import PostForm, CommentForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    try:
        req = json.loads(request.body)
        post_id = req.get('id')
        button_type = req.get('type')

        post = Posts.objects.get(id=post_id)

        if button_type == 'like':
            post.like += 1  # 좋아요 증가
        elif button_type == 'dislike':
            post.dislike += 1  # 싫어요 증가
        else:
            return JsonResponse({'error': 'Invalid button type'}, status=400)

        post.save()

        return JsonResponse({'id': post_id, 'type': button_type, 'count': getattr(post, button_type)})
    except Posts.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def pirostagram_list(request):
    posts = Posts.objects.all().order_by('-created_at')  
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Posts, id=id)
    comments = post.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user  # 댓글 작성자 설정
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pirostagram_list')
        else:
            print(form.errors)
    else:
        form=PostForm()
    return render(request, 'posts/post_create.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Posts, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('pirostagram_list')  
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form, 'post': post})

def post_delete(request, id):
    post = get_object_or_404(Posts, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('pirostagram_list')  
    return redirect('post_detail', id=id)
