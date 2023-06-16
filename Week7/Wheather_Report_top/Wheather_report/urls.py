
from django.contrib import admin
from django.urls import path, include
from weatherapp.views import ReportListView, ReportDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/reports/", ReportListView.as_view(), name="reports"),
    # path("api/reports/<int:pk>", ReportDetailView.as_view(), name="reports-detail"),
    path(
        "api/reports/<int:pk>", ReportDeleteView.as_view(), name="reports-detail-delete"
    ),
    # path("api/reports/", ReportView.as_view(), name="reports"),
    # path("api/reports/<int:pk>", ReportView.as_view(), name="report-detail"),
]