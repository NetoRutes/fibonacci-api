from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Fibonacci API",
        default_version='v1',
        description="API for calculating and storing Fibonacci numbers.",
        contact=openapi.Contact(email="netorutes@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

swagger_urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]