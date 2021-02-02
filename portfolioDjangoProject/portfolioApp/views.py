from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def resume(request):
    return render(request,'resume.html')

def work(request):
    return render(request,'work.html')

def life(request):
    return render(request,'life.html')

# Create your views here.
