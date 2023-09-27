from django.shortcuts import render

# Create your views here.
def reading(request):
    return render(request, 'speaking/speaking.html')