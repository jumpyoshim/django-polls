from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from django.contrib import messages
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import ChoiceFormSet, QuestionForm
from .models import Choice, Question
from .serializers import ChoiceSerializer


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'polls/list.html'


class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['choices'] = Choice.objects.filter(question_id=self.object.pk).order_by('pk')
        return data


class QuestionCreateView(CreateView):
    form_class = QuestionForm
    template_name = 'polls/form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['choices'] = ChoiceFormSet(self.request.POST)
        else:
            data['choices'] = ChoiceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        choices = context['choices']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if choices.is_valid():
                choices.instance = self.object
                choices.save()
        messages.success(self.request, 'Question is created.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('polls:detail', kwargs={'pk': self.object.pk})


class VoteView(RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get(self, request, *args, **kwargs):
        choice = self.get_object()
        serializer = self.get_serializer(choice)
        choice.votes += 1
        choice.save()
        return Response(serializer.data)
