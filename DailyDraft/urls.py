"""
URL configuration for DailyDraft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view=views.Home, name='home'),
    path('login/', view=views.Login, name='login'),
    path('register/', view=views.Register, name='register'),
    path('pricing/', view=views.Pricing, name='pricing'),
    path('build/', view=views.Build, name='build'),
    path('drafts/', view=views.Drafts, name='drafts'),
    path('search/', view=views.search, name='search'),
]
