"""trade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import MainView, buy, sell_market, sell_limit, NewDesign

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('buy/', buy),
    path('sell_market/', sell_market),
    path('sell_limit/', sell_limit),
    path('new_design', NewDesign.as_view())
] + staticfiles_urlpatterns()
