from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:
    
    @tail_call_optimized
    def fibonacci_tail_recursion(n: int, index: int = 0, previous: int = 0, next: int = 1):
        if index == n:
            return previous
        
        return fibonacci_tail_recursion(n, index + 1, next, previous + next)
    
    return fibonacci_tail_recursion

