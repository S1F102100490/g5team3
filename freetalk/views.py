from django.shortcuts import render

def freetalk(request):
    return render(request, 'freetalk/FreeTalk.html')