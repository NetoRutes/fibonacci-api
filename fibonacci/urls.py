from django.urls import path
from .views import FibonacciView

urlpatterns = [
    path('generate/', FibonacciView.as_view(), name='generate_fibonacci'),
]
