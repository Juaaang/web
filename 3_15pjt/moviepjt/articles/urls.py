from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('hello/<str:name>/<int:age>/', views.hello, name='hello'),
    path('index/', views.index, name='index'),
]