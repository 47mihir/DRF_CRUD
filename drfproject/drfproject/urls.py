from django.contrib import admin
from django.urls import path
from appdrf import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('personapi/', views.person_api),
    path('personapi/<int:pk>', views.person_api),
]
