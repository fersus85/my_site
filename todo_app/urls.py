from django.urls import path
from todo_app import views as vs

urlpatterns = [
    path("", vs.MainListView.as_view(), name="index"),
    path("<int:list_id>/", vs.ItemListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path("add/", vs.ListCreate.as_view(), name="list-add"),
    path("<int:pk>/delete/", vs.ListDelete.as_view(), name="list-delete"),
    # CRUD patterns for ToDoItems
    path(
        "<int:list_id>/item/add/",
        vs.ItemCreate.as_view(),
        name="item-add",
    ),
    path(
        "<int:list_id>/item/<int:pk>/",
        vs.ItemUpdate.as_view(),
        name="item-update",
    ),
    path(
        "<int:list_id>/item/<int:pk>/delete/",
        vs.ItemDelete.as_view(),
        name="item-delete",
    ),
]
