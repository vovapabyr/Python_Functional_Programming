from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, __value: object) -> bool:
        return self.value == __value.value

def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:

    def is_pure_int(input: Integer):
        # Checks if a new instance is created => no assignemnts done to input  
        if input is increment_fn(input):
            return False

        # Checks if there is no dependency on outer context (ex. cache)
        if increment_fn(input) is increment_fn(input):
            return False 

        # Checks that the function always return the same value for the same input 
        return increment_fn(input) == increment_fn(input)
    
    return is_pure_int(Integer(1))
        