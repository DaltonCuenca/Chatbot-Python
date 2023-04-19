from django.http import HttpResponse
from django.shortcuts import render

def chatView(request):
    return render(request, 'chat/index.html')