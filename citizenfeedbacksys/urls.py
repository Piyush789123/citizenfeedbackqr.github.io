"""citizenfeedbacksys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include

from mainapp.views import bar_graph, home,adm,mainadm,otp_verify,feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('custom-login/',adm,name='custom_login'),
    path('stats/',mainadm,name='admin_page'),
    path('otp/',otp_verify,name='otp'),
    path('captcha',include("captcha.urls")),
    path('feedback/',feedback,name='fb_form'),
    # path('feedbacks/',feedbacks,name='feedbacks'),
    path('bar-graph/',bar_graph,name='bar_graph'),
]
