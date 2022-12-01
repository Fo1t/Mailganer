from django.shortcuts import render

def MainStatPage(request):
    return render(request, 'index.html')