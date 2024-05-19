from django.shortcuts import get_object_or_404, render
#from django.shortcuts import render
from django.http import Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'content/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'content/detail.html', {'question': question})
# Create your views here.
