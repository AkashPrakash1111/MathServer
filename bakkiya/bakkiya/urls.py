from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculatepower/', views.calculate_power, name="calculate_power"),
    path('', views.calculate_power, name="calculate_power_home")
]
