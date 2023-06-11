from django.contrib import admin
from django.urls import path, include
from students.views import students_list, students_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('students/', students_list, name='students-list'),
    path('students/<int:pk>/', students_detail, name='students-detail'),
]
