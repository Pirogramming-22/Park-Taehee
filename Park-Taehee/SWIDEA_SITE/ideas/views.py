from django.shortcuts import render, get_object_or_404, redirect
from .models import Ideas
from .forms import IdeaForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def idea_list(request):
    sort_by = request.GET.get('sort_by', 'interest')  # 기본값 'interest'
    if sort_by == 'interest':
        ideas = Ideas.objects.order_by('-interest')  # 관심도 기준 내림차순 정렬
    # 'name'으로 정렬
    elif sort_by == 'name':
        ideas = Ideas.objects.order_by('title')  # 이름 기준 오름차순 정렬
    # 'created_at'으로 정렬 (등록순)
    elif sort_by == 'created_at':
        ideas = Ideas.objects.order_by('created_at')  # 등록순, 오름차순 정렬
    # 'latest'으로 정렬 (최신순)
    elif sort_by == 'latest':
        ideas = Ideas.objects.order_by('-created_at')  # 최신순, 내림차순 정렬
    else:
        ideas = Ideas.objects.all() 

    return render(request, 'ideas/idea_list.html', {'ideas': ideas, 'sort_by': sort_by})


def idea_detail(request, id):
    idea = get_object_or_404(Ideas, id=id)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})


def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('idea_list')
        else:
            print(form.errors)
        
    else:
        form=IdeaForm()
    return render(request, 'ideas/idea_create.html', {'form': form})

def idea_edit(request, id):
    idea = get_object_or_404(Ideas, id=id)
    if request.method == 'POST':
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', id=idea.id)
    else:
        form = IdeaForm(instance=idea)
        
    return render(request, 'ideas/idea_edit.html', {'form': form, 'idea': idea})


def idea_delete(request, id):
    idea = get_object_or_404(Ideas, id=id)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')  # 삭제 후 목록 페이지로 리다이렉트
    return redirect('idea_detail', id=id)  # 다른 방법으로 접근하면 상세 페이지로 리다이렉트


@csrf_exempt
def update_interest(request, idea_id):
    if request.method == "POST":
        data = json.loads(request.body)
        interest = data.get('interest')
        try:
            idea = Ideas.objects.get(id=idea_id)
            idea.interest = interest
            idea.save()
            return JsonResponse({'status': 'success', 'interest': interest})
        except Ideas.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Idea not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update_star(request, idea_id):
    if request.method == "POST":
        data = json.loads(request.body)
        is_starred = data.get('is_starred', False)

        try:
            idea = Idea.objects.get(id=idea_id)
            idea.stars = 1 if is_starred else 0  # 별 상태를 숫자로 저장
            idea.save()
            return JsonResponse({"success": True, "stars": idea.stars})
        except Idea.DoesNotExist:
            return JsonResponse({"success": False, "error": "Idea not found"})
    return JsonResponse({"success": False, "error": "Invalid request method"})


def get_star_states(request):
    # 예시: 모든 아이디어의 별 상태를 반환
    ideas = Idea.objects.all()
    star_states = []

    for idea in ideas:
        star_states.append({
            'id': idea.id,
            'stars': idea.stars  # 별의 개수를 또는 상태를 반환
        })
    
    return JsonResponse({'star_states': star_states})