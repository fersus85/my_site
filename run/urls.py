from django.urls import path
from run import views

urlpatterns = [
    path("run/", views.RunListView.as_view(), name="run_home"),
    path("new_year/", views.RunYearCreateView.as_view(), name="new_year"),
    path("new_month/", views.RunMontCreateView.as_view(), name="new_month"),
]
