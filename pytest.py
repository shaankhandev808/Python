"""
Pytest finds test files, runs functions whose names start with test_ 
and reports whether assertions pass or fail.

Sample main module to test:
from dataclasses import dataclass

@dataclass(slots=True)
class Player:
    name: str
    health: int
    x: float
    y: float

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health < 0:
            self.health = 0

Sample            
            
            
"""

