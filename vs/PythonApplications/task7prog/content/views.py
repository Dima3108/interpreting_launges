
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import Http404
#from .models import Question
from django.http import HttpResponse
from django.template import loader
from pindex import *
def index(requets):
    c=get_content()
    html = "<html><body>It is now %s.</body></html>" % c
    return HttpResponse(html)
    #return redirect("Content/Pages/Index.py")
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'content/index.html', context)
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'content/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
