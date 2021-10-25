from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# class MakeQuestionView(generic.TemplateView):
#     template_name = 'polls/make_question.html'

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # def get_object(self):
    #     object = get_object_or_404(Question, id=self.kwargs['id'])
    #     return object


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def make_question(request):
    if request.method == 'GET':
        return render(request, 'polls/make_question.html')
    if request.method == 'POST':
        question = Question()
        question.question_text = request.POST['question_text']
        question.pub_date = timezone.now()
        choice_1 = Choice()
        choice_2 = Choice()
        choice_3 = Choice()

        choice_1.choice_text = request.POST['choice_1']
        choice_2.choice_text = request.POST['choice_2']
        choice_3.choice_text = request.POST['choice_3']
        choice_1.votes = 0
        choice_2.votes = 0
        choice_3.votes = 0
        choice_1.question = question
        choice_2.question = question
        choice_3.question = question

        question.save()
        choice_1.save()
        choice_2.save()
        choice_3.save()
        return redirect(reverse('polls:index'))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
        {'question' : question,
         'error_message' : 'You didn`t select a choice.'})

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))