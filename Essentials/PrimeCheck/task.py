from math import ceil, sqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    def is_prime_int(factor: int):
        if factor == 1:
            return True
        
        return n % factor != 0 and is_prime_int(factor - 1) 

    # Check till sqrt(n) as a larger factor of n must be a multiple of a smaller factor that has been already checked
    return is_prime_int(ceil(sqrt(n)))