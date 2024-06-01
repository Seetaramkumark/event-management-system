"""evmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

admin.site.site_header = 'Event Manager Head'
admin.site.site_title = 'Event Manager Head'
admin.site.index_header = 'Event Management Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.login,name="login"),
    path("default1", views.default1, name="home"),
    path("signin", views.signin, name="signin"),
    path("booking", views.booking, name="booking"),
    path("payment", views.payment, name="payment"),
    path("sucess", views.sucess, name="sucess"),
    path("userevents/",views.usereventsfunction,name="userevents"),
    path("userhome/",views.userhomefunction,name="userhome"),
    path("userorders/",views.userordersfunction,name="userorders"),
    path("userfeedback",views.userfeedbackfunction,name="userfeedback"),
    path("contactrequest",views.contactrequest,name="reuest"),
    path("html",views.htmlpage, name="html")
]