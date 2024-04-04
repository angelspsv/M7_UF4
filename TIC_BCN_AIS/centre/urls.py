from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('students/student/<str:pk>/', views.student, name='student'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/teacher/<str:pk>/', views.teacher, name='teacher'),
    path('form/', views.form, name='form'),
    path('display/', views.display_data, name='display_data')
]