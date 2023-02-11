from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    raise Exception('Implement me')