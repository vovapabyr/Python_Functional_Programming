from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized

def factorial_impl() -> Callable[[int], int]:

    @tail_call_optimized     
    def factorial_tail_recursion(x: int, acc: int = 1):
        if(x <= 1):
            return acc

        return factorial_tail_recursion(x - 1, acc * x)

    return factorial_tail_recursion
    
