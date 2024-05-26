import sys
import sqlite3
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import Http404
#from .models import Question
from django.http import HttpResponse
from django.template import loader
def get_content():
    connection = sqlite3.connect('painting_database.db')
    content=""
    cursor = connection.cursor()
    cursor.execute("SELECT type FROM type_of_painting")

    for elem in cursor.fetchall():
        content=content+"<div>"+str(elem)+"</div>\n"
    content=content+'''
        </div>
      
       </div>
       <div>
        <strong>Авторы:</strong>
        <div id="acontent">
      '''
    #Содержимое бд
    cursor = connection.cursor()
    cursor.execute("SELECT author FROM authors")  
    for elem in cursor.fetchall():
       content=content+"<div>"+str(elem)+"</div>\n"
       #print("<div> %s</div>\n" %(elem))
    content=content+'''
        </div>
         <div>
          <strong>
            Картины
          </strong>
          <div id="imcontent">
'''
    cursor = connection.cursor()
    cursor.execute("SELECT authors.author ,type_of_painting.type,iatp.name  FROM authors,iatp,type_of_painting"+
               " WHERE iatp.type = type_of_painting.id and iatp.authorid = authors.id")
    content=content+'''
    <table style="position: relative;display: flex; justify-content: center;border: 2px solid blue;text-align: center; ">
      <tr style="background-color:blueviolet; font-size:xx-large">
         <th>Название картины</td>
         <th>Вид картины</td>
         <th>Автор картины</td>
      </tr>
'''
    for elem in cursor.fetchall():
    #print(
      content=content+'''
    <tr class="trow">
          <td>'''+str(elem[2])+'''</td>
          <td>'''+str(elem[1])+'''</td>
          <td>'''+str(elem[0])+'''</td>
    </tr>\n
    '''
    content=content+'''
    </table>
      <style>
            .trow {
               font-size: x-large;
               background-color: aquamarine;
               text-align: center;
               
            }
     </style>
'''
    content=content+'''
          </div>
        </div>
       </div>
       
    </main>
</body>
''' 
    connection.close()
    return content


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
