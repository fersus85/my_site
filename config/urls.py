"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from config import settings
from todo_app.views import MainPage, contact_view, success_view
from system.views import tr_handler403, tr_handler404, tr_handler500


handler403 = tr_handler403
handler404 = tr_handler404
handler500 = tr_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path('captcha/', include('captcha.urls')),
    path("", include("todo_app.urls")),
    path("", include("blog.urls")),
    path("", include("run.urls")),
    path("", include("read.urls")),
    path("", MainPage.as_view(), name='home'),
    path('feedback/', contact_view, name='feedback'),
    path('success/', success_view, name='success'),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
