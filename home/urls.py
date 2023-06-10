from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "VisionX Admin"
admin.site.site_title = "VisionX Admin Portal"
admin.site.index_title = "Welcome to VisionX Portal"

urlpatterns = [
    path("", views.index, name='home'),
]