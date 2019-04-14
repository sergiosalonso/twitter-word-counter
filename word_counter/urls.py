from django.urls import path
from . import views
app_name= 'word-counter'

urlpatterns = [
    path('', views.form_name_view, name='form'),
]
