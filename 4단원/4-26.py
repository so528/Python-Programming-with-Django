from django.urls import path
from . import views
from myapp.views import MyView
form some_app.views import AboutView

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('my-form/', views.my_form_view, name='my_form'),
    path('about/', MyView.as_view()),
    path('about/' , AboutView.as_view()),
]