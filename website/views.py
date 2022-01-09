from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def mainframe(request):

    return render(request, 'mainframe.html')