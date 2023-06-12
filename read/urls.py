from django.urls import path
from read import views

urlpatterns = [
    path("read/", views.ReadListView.as_view(), name="read_home"),
    path("read/<int:year_id>/", views.YearListView.as_view(), name="read_year"),
    path("read/new_year/", views.YearCreateView.as_view(), name="year_new"),
    path("read/new_book/", views.BookCreateView.as_view(), name="book_new"),
]
