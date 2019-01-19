"""simple_votings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from vote import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.index_page, name="index"),
    path('404/', views.not_found, name="404"),

    path('report/', views.report, name="report"),
    path('report_status/', views.report_status, name="report_status"),

    path('create_vote/', views.create_vote, name="create_vote"),
    path('vote/', views.vote, name='vote'),
    path('search_vote/', views.search_page, name="search_vote"),
    url(r'^vote/(?P<pk>[\w\d-]+)$', views.vote),

    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('sign_up/', views.sign_up, name="sign_up"),

    path('contacts/', views.contacts, name="contacts"),
    path('support/', views.support, name="support"),

    path('profile/', views.profile, name="profile"),
    path('profile/my_votings/', views.my_votings, name="my_votings"),
    path('profile/votings_i_answered/', views.votings_i_answered, name="votings_i_answered"),
    path('profile/edit', views.profile_edit, name="profile_edit"),
]

