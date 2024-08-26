from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator

n_value_parameter = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'n_value': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of terms of the Fibonacci sequence to be generated.', example=10)
    },
    required=['n_value'],
)

def fibonacci_decorator(cls):
    @method_decorator(
        swagger_auto_schema(
            request_body=n_value_parameter,
            responses={200: 'Fibonacci sequence successfully generated'}
        ),
        name='post'
    )
    class Wrapped(cls):
        pass
    
    return Wrapped
