from typing import Optional


class Car:
    def __init__(self, vin: int, speed: int) -> None:
        self.VIN: int = vin
        self.speed: int = speed
        self.engine_cap: Optional[int] = None
        self.price: Optional[int] = None
        self.brand: Optional[str] = None

