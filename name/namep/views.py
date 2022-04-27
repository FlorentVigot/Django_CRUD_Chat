from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from namep.models import Question
from .forms import Question

def index(request):
    questions = Question.objects.all()
    context = {'questions' : questions,}
    return render(request, 'namep/post.html', context)


def post(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = Question(request.POST or None)
    if form.is_valid():
        form.save()
        
    context['form']= form
    return render(request, "post.html", context)

def put(request, id=None):
    questions = Question.objects.all()
    context = {'questions' : questions,}
    return render(request, 'namep/put.html', context)


def delete(request, id):
    
    context = {}
 
    # fetch the object related to passed id
    question = get_object_or_404(Question, id = id)
 
 
    if request.method =="POST":
        # delete object
        question.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "namep/delete.html", context)