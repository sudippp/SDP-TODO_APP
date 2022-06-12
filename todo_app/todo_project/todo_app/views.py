from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    fm = TodoModelForm()
    context = {'fm':fm}
    todomodel = TodoModel.objects.all()
    context['todomodel'] = todomodel
    print(todomodel)
    if request.method == "POST":
        fm = TodoModelForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your Task is SAVED !!')
            
    return render( request,'index.html',context)


def modify(request,pk=0):
    tm = TodoModel.objects.get(id=pk)
    fm = TodoModelForm(instance=tm)
    context = {'fm':fm}
    todomodel = TodoModel.objects.all()
    context['todomodel'] = todomodel
    if request.method == "POST":
        fm = TodoModelForm(request.POST, instance=tm)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your Task is UPDATED !!')
    return render( request,'modify.html',context)


def delete(request,pk=0):
    tm = TodoModel.objects.get(id=pk)
    tm.delete()
    return redirect('/')


def text(request):
    return render(request,'index2.html')