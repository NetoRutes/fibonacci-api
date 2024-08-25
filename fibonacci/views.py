from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FibonacciNumber
from .serializers import FibonacciNumberSerializer

def calculate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

class FibonacciView(APIView):
    def post(self, request):
        try:
            n_value = int(request.data.get('n_value'))
        except (TypeError, ValueError):
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        fib_obj, created = FibonacciNumber.objects.get_or_create(n_value=n_value)

        if created:
            # If it does not exist, calculate the sequence and save
            fib_sequence = calculate_fibonacci(n_value)
            fib_obj.fibonacci_sequence = ','.join(map(str, fib_sequence))
            fib_obj.save()

        serializer = FibonacciNumberSerializer(fib_obj)
        return Response(serializer.data)