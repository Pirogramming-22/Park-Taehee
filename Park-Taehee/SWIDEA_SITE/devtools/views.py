from django.shortcuts import render, get_object_or_404, redirect
from .models import DevTools
from devtools.forms import DevToolForm

def devtool_list(request):
    devtools = DevTools.objects.all()
    return render(request, 'devtools/devtool_list.html', {'devtools': devtools})

def devtool_detail(request, id):
    devtool = get_object_or_404(DevTools, id=id)
    return render(request, 'devtools/devtool_detail.html', {'devtool': devtool})


def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('devtool_list')
        else:
            print(form.errors)
        
    else:
        form=DevToolForm()
    return render(request, 'devtools/devtool_create.html', {'form': form})

def devtool_edit(request, id):
    devtool = get_object_or_404(DevTools, id=id)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtool_detail', id=devtool.id)
    else:
        form = DevToolForm(instance=devtool)
        
    return render(request, 'devtools/devtool_edit.html', {'form': form, 'devtool': devtool})


def devtool_delete(request, id):
    devtool = get_object_or_404(DevTools, id=id)
    if request.method == 'POST':
        devtool.delete()
        return redirect('devtool_list')
    return redirect('devtool_detail', id=id)