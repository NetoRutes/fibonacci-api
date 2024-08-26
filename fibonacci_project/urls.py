from django.contrib import admin
from django.urls import path, include
from fibonacci_project.swagger import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',  include('fibonacci.urls')),
    *swagger_urlpatterns,
]
