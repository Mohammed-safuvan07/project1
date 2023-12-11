from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.register,name='register'),
    path('class_det/',views.class_det,name='class_det'),
    path('student_det/',views.student_det,name='student_det'),
    path('details/',views.details,name='details'),
]
