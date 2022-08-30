
from django.contrib import admin
from django.urls import path
from appdjango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personapi/', views.person_api),
    # path('all/', views.person_list),
]
