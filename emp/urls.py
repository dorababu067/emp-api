from django.urls import path
from .views import EmployeeAPIView, EmployeeDetailAPIView

urlpatterns = [
    path("employees/", EmployeeAPIView.as_view(), name="employee"),
    path(
        "employees/<int:pk>/", EmployeeDetailAPIView.as_view(), name="employee_detail"
    ),
]
