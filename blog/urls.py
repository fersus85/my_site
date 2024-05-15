from django.urls import path
from blog import views as vs


urlpatterns = [
    path("home/", vs.BlogListView.as_view(), name="blog_home"),
    path("new/", vs.BlogCreateView.as_view(), name="post_new"),
    path("<slug:slug>/", vs.BlogDetailView.as_view(), name="post_detail"),
    path("edit/<slug:slug>/", vs.BlogUpdateView.as_view(), name="post_edit"),
    path("delete/<slug:slug>", vs.BlogDeleteView.as_view(), name="post_delete")
]
