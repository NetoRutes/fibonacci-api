from django.db import models

class FibonacciNumber(models.Model):
    n_value = models.IntegerField(unique=True)
    fibonacci_sequence = models.TextField()

    def __str__(self):
        return f'Fibonacci sequence for n={self.n_value}'