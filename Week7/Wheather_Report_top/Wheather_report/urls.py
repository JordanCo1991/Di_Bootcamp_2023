from django.contrib import admin
from django.urls import path, include
from report.views import ReportView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/report/', ReportView.as_view(),name = 'reports'),
    path('api/report>int:pk>', ReportView.as_view(),name = 'reports')
]