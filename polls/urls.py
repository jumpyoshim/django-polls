from django.urls import path

from .views import QuestionCreateView, QuestionDetailView, QuestionListView, VoteView

app_name = 'polls'
urlpatterns = [
    path('', QuestionListView.as_view(), name='list'),
    path('new/', QuestionCreateView.as_view(), name='create'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='detail'),
    path('vote/<int:pk>/', VoteView.as_view(), name='vote'),
]
