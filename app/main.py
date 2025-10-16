from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __sub__(self, number: int) -> int:
        self.health -= number
        if self.health <= 0:
            print(1)
            Animal.alive.remove(self)
        return self.health

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True if self.hidden is False else False


class Carnivore(Animal):
    @classmethod
    def bite(cls, animal: Animal | Herbivore | Carnivore) -> None:
        if animal.hidden is False and not isinstance(animal, Carnivore):
            animal -= 50
