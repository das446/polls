from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Question
from django.views import generic
from django.utils import timezone

from .models import *
from django import forms
from django .forms import formset_factory


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class CreateView(generic.ListView):
    template_name = 'polls/create.html'
    context_object_name = 'create_question'
    def get_queryset(self):
        return Question.objects


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class EditView(generic.DetailView):
    model = Question
    template_name = 'polls/edit.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    print(request)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        vote=Vote.get(q=question,c=selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        vote.votes += 1
        vote.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def edit(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    question.question_text=request.POST['question_text']
    question.removeAllChoices()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def create(request):
    question=Question(question_text=request.POST['question_text'])
    question.pub_date=timezone.now()
    choice_count=int(request.POST['choice_count'])
    print(choice_count)

    for x in range(0,choice_count):
        name='choice'+str(x)
        choice=Choice(choice_text=request.POST[name])
        Vote.addVote(q=question,c=choice, amnt=0)

    list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    context_object_name = {'latest_question_list': list}
    return render(request, 'polls/index.html', context_object_name)



def delete(request, question_id):
    question=Question.objects.get(id=question_id)
    question.delete()

    list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    context_object_name = {'latest_question_list': list}
    return render(request, 'polls/index.html', context_object_name)

def get_index(self,request): #replacing the 3 lines above with this function doesn't work for some reason
    list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    context_object_name = {'latest_question_list': list}
    return render(request, 'polls/index.html', context_object_name)