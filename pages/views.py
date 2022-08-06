from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request,'pages/welcome_page.html',{})

def analyseResult(request):
    return render(request,'pages/analyse.html',{})