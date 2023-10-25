from django.shortcuts import render



def speaking(request):

    return render(request, 'speaking/speaking.html')
