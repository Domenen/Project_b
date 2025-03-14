from django.shortcuts import render
from django.views import View

def hello(request, name='John'):
    context = {'name': name}
    return render(request, 'hello.html', context)


class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'feedback.html')
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        context = {}
        context["name"] = data["name"]
        context["user_feedback"] = data["user_feedback"]
        return render(request, 'feedback_send.html', context)