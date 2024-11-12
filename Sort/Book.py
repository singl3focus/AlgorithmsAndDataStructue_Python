from typing import Optional


class Book:
    def __init__(self, ISBN: str, price: int):
        self.ISBN: str = ISBN
        self.price: int = price
        self.author: Optional[str] = None
        self.capacity: Optional[str] = None
        self.producer: Optional[str] = None