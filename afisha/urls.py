from django.contrib import admin
from django.urls import path
from afisha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start_page)
]
