from django.shortcuts import render

def freetalk(request):
    return render(request, 'reading/FreeTalk.html')