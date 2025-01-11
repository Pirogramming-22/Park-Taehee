from django.shortcuts import render, get_object_or_404, redirect
from .models import Reviews
from .forms import ReviewForm
# Create your views here.

def review_list(request):
    sort_by = request.GET.get('sort_by', 'title')  
    if sort_by == 'score':
        reviews = Reviews.objects.all().order_by('-score')  
    elif sort_by == 'time':
        reviews = Reviews.objects.all().order_by('time')  
    else:
        reviews = Reviews.objects.all().order_by('title')  

    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, id):
    review = get_object_or_404(Reviews, id=id)
    hours = review.time // 60
    minutes = review.time % 60
    return render(request, 'reviews/review_detail.html', {'review': review, 'hours': hours, 'minutes': minutes})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
        
    else:
        form=ReviewForm()
    return render(request, 'reviews/review_create.html', {'form': form})

def review_edit(request, id):
    review = get_object_or_404(Reviews, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', id=review.id)
    else:
        form = ReviewForm(instance=review)
        
    return render(request, 'reviews/review_edit.html', {'form': form, 'review': review})

def review_delete(request, id):
    review = get_object_or_404(Reviews, id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return redirect('review_detail', id=id)
