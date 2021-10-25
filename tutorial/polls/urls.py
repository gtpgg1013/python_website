from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('make_question/', views.make_question, name='make_question'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
