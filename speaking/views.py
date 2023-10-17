from django.shortcuts import render

# Create your views here.
def speaking(request):
    return render(request, 'speaking/speaking.html')
