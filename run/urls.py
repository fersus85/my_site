from django.urls import path
from run import views as vs

urlpatterns = [
    path("", vs.RunListView.as_view(), name="run_home"),
    path("new_year/", vs.RunYearCreateView.as_view(), name="new_year"),
    path("year_list/", vs.RunYearListView.as_view(), name="year_list"),
    path("<int:pk>/delete_year/", vs.RunDelView.as_view(), name="delete_year"),
    path("<int:pk>/edit_year/", vs.RunUpdateView.as_view(), name="edit_year"),
]
