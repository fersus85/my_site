from django.urls import path
from blog import views

urlpatterns = [
    path("blog/", views.BlogListView.as_view(), name="blog_home"),
    path("post/<int:pk>/", views.BlogDetailView.as_view(), name="post_detail")
]
