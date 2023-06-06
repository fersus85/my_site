from django.urls import path
from run import views

urlpatterns = [
    path("run/", views.RunListView.as_view(), name="run_home"),
    path("new_year/", views.RunYearCreateView.as_view(), name="new_year"),
    path("new_month/", views.RunMontCreateView.as_view(), name="new_month"),
    path("<int:pk>/delete_year/", views.RunYearDeleteView.as_view(), name="delete_year"),
    path("<int:pk>/edit_year/", views.RunYearUpdateView.as_view(), name="edit_year"),
    path("year_list/", views.RunYearListView.as_view(), name="year_list"),
    path("<int:pk>/", views.RunDetailView.as_view(), name="detail_year"),
]
