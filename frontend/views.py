from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'frontend/index.html')



def works(request):

    return render(request, 'frontend/works.html')

def hireMe(request):

    return render(request, 'frontend/hireMe.html')

def about(request):

    return render(request, 'frontend/about.html')

def hobby(request):

    return render(request, 'frontend/hobby.html')

def hobbies(request):

    return render(request, 'frontend/hobbies.html')

def ww(request):

    return render(request, 'frontend/ww.html')