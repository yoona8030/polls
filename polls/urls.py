from django.urls import path
from . import views

app_name = 'polls'

## funtion-based view
# urlpatterns=[
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]

## Generic view
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    # ex_ /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #ex_ /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #ex_ /polls/2/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]