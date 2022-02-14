
from django.urls import path
from .views import internship_list, internship_detail

urlpatterns = [
    path("intern/", internship_list),
    path("detail/<int:pk>/", internship_detail)
]
