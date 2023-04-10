from typing import Callable


def fibonacci_impl() -> Callable[[int], int]:

    def fibonacci(x: int):
         if (x < 2):
            return x
         
         return fibonacci(x - 1) + fibonacci(x - 2)
    
    return fibonacci
