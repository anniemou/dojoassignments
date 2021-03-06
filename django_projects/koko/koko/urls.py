"""koko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^blogs/', include('apps.blogs_app.urls')),
    url(r'^timedisplay/', include('apps.time_display.urls')),
    url(r'^random_word/', include('apps.Randow_Word_Generator.urls')),
    url(r'^surveys/', include('apps.surveys.urls')),
    url(r'^session_words/', include('apps.session_words.urls')),
    url(r'^book_authors/', include('apps.book_authors.urls')),
    url(r'^dojo_ninjas/', include('apps.dojo_ninjasn.urls')),
    url(r'^login/', include('apps.login_registration.urls')),

]
