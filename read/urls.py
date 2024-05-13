from django.urls import path
from read import views
from django.views.decorators.cache import cache_page

urlpatterns = [
     path("",
          cache_page(15)(views.HomeListView.as_view()),
          name="read_home"),
     # year
     path("<int:year_id>/",
          views.YearListView.as_view(),
          name="read_year"),
     path("new_year/", views.YearCreateView.as_view(), name="year_new"),
     path("year_list/", views.YearEditListView.as_view(), name="year_list"),
     path("delete/<int:pk>/", views.YearDeleteView.as_view(),
          name='del_read_year'),
     path("update/<int:pk>/", views.YearEditView.as_view(),
          name='edit_read_year'),
     # book
     path("new_book/", views.BookCreateView.as_view(), name="book_new"),
     path("del_book/<int:pk>/", views.BookDeleteView.as_view(),
          name='delete_book'),
     path("upd_book/<int:pk>/", views.BookUpdView.as_view(),
          name='update_book'),
]
