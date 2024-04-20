from django.contrib import admin
from django.urls import path
from app import views as appview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',appview.home,name='home')
]
