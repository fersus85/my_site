from django.urls import path
from run import views

urlpatterns = [
    path("run/", views.RunListView.as_view(), name="run_home"),
    # path("post/<int:pk>/", views.BlogDetailView.as_view(), name="post_detail"),
    # path("post/new/", views.BlogCreateView.as_view(), name="post_new"),
    # path("post/<int:pk>/edit/", views.BlogUpdateView.as_view(), name="post_edit"),
    # path("post/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="post_delete"),
]
