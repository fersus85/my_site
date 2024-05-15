from django.urls import path
from read import views as vs
from django.views.decorators.cache import cache_page

urlpatterns = [
     path("",
          cache_page(15)(vs.HomeListView.as_view()), name="read_home"),
     # year
     path("<int:year_id>/", vs.YearListView.as_view(), name="read_year"),
     path("new_year/", vs.YearCreateView.as_view(), name="year_new"),
     path("year_list/", vs.YearEditListView.as_view(), name="year_list"),
     path("delete/<int:pk>/", vs.YearDeleteView.as_view(), name='del_year'),
     path("update/<int:pk>/", vs.YearEditView.as_view(), name='edit_year'),
     # book
     path("new_book/", vs.BookCreateView.as_view(), name="book_new"),
     path("del_book/<int:pk>/", vs.BookDeleteView.as_view(), name='del_book'),
     path("upd_book/<int:pk>/", vs.BookUpdView.as_view(), name='update_book'),
]
