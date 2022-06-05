from django.urls import path

from . import views
<<<<<<< HEAD

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
=======
urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
>>>>>>> a2fea69c6da2abeacdb50efd624499589ef1fb3f
]
