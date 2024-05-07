from django.urls import path
from blog import views

urlpatterns = [
    path("blog/", views.BlogListView.as_view(),
         name="blog_home"),
    path("post/new/", views.BlogCreateView.as_view(),
         name="post_new"),
    path("post/<slug:post_slug>/", views.BlogDetailView.as_view(),
         name="post_detail"),
    path("post/edit/<slug:post_slug>/", views.BlogUpdateView.as_view(),
         name="post_edit"),
    path("post/delete/<slug:post_slug>", views.BlogDeleteView.as_view(),
         name="post_delete"),
]
