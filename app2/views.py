from django.shortcuts import render

# Create your views here.
def conditions(request):
    dict = {'a':100, 'b':200, 'c':300, 'd':600}
    return render(request,'conditions.html',dict)