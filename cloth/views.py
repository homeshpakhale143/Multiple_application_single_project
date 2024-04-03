from django.shortcuts import render

# Create your views here.
def tracks(request):
    return render(request,'tracks.html')