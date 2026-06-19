from app.nature.animal import Animal
from app.nature.herbivore import Herbivore


class Carnivore(Animal):
    @classmethod
    def bite(cls, animal: Herbivore) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                cls.alive.remove(animal)
