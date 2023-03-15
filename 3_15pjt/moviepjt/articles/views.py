from django.shortcuts import render

# Create your views here.
def hello(request, name, age):
    person = {
        'name': name,
        'age':age,
    }
    
    context = {
        'person':person,
    }
    return render(request, 'articles/hello.html', context)

def index(request):
    return render(request, 'articles/index.html')