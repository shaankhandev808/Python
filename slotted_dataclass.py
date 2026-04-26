"""
Slotted dataclass = Structs in C. 
# 
# Slotted dataclass offers us a way to maintain and update 
# state in a way that is even quicker than dicts. 
# A struct is a custom grouping of data types -- this
# is in contrast to an array, where everything is of
# the same type. We can set up a dataclass / struct 
# in Python to use a contiguous block of memory such 
# that reads and updates are quicker than even hash
# tables, that involve a lookup. 

# Dict-backed object: “Find the key named health, then 
# return its value.”

Slotted object: “Go straight to the reserved place for 
health.”

This is why slotted dataclasses are faster than dicts. 

Now lets see dataclass in action.

"""

from dataclasses import dataclass

@dataclass(slots=True) # Decorator gives initializer. 
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

def main():
    player = Player(name="Hero", health=79, x=10.0, y=20.0)

    print("Start:", player)

    player.move(5.0, -3.0)
    player.take_damage(25)

    print("After update:", player)
    print("Name:", player.name)
    print("Health:", player.health)
    print("Position:", (player.x, player.y))

    # Because slots are enabled, adding brand-new attributes is not allowed.
    try:
        player.score = 999
    except AttributeError as e:
        print("AttributeError:", e)

    second_player = Player("Shaan", 120, 12, 12)

    print("Name: " + second_player.name)

if __name__ == "__main__":
    main()