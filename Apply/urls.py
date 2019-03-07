from django.urls import path
from . import views

app_name = 'Apply'
urlpatterns = [
    path('Submit', views.submit, name='submit'),
    path('Evaluation/<int:apply_id>', views.evaluation, name='evaluation'),
    path('List', views.apply_list, name='list'),
    path('Details/<int:apply_id>', views.detail, name='detail'),
]