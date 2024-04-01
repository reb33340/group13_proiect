class Fibonacci:
    def __init__(self):
        self.a = {}

    def fibonacci(self, n):
        if n in self.a:
            return self.a[n]
        if n <= 1:
            return n
        result = self.fibonacci(n-1) + self.fibonacci(n-2)
        self.a[n] = result
        return result
