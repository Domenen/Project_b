from django.shortcuts import render

def hello(request):
    name = 'John'
    context = {'name': name}
    return render(request, 'hello.html', context)