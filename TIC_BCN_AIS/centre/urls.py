from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('students/student/<str:pk>/', views.student, name='student'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/teacher/<str:pk>/', views.teacher, name='teacher'),
    path('form/', views.form, name='form'),
    path('display/', views.display_data, name='display_data'),
    path('update/<str:pk>/', views.update_user, name='update_user'),
    path('teachers/update/<str:pk>/', views.update_user, name='update_teacher'),
    path('students/update/<str:pk>/', views.update_user, name='update_student'),
    path('delete/<str:pk>/', views.delete_user, name='delete_user')
]