from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("html/", views.html_index, name="html_index"),
    path("profile/", views.profile, name="profile"),
    path("contact/", views.contact, name="contact"),
]