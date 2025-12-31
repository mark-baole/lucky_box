import random
from typing import List, Optional, Dict
from enum import Enum

class Rarity(str, Enum):
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"

class Animal:
    def __init__(self, name: str, emoji: str, rarity: Rarity, image_url: Optional[str] = None):
        self.name = name
        self.emoji = emoji
        self.rarity = rarity
        self.image_url = image_url

ANIMALS = [
    Animal("Lion", "🦁", Rarity.RARE),
    Animal("Elephant", "🐘", Rarity.RARE),
    Animal("Monkey", "🐒", Rarity.COMMON),
    Animal("Panda", "🐼", Rarity.RARE),
    Animal("Tiger", "🐯", Rarity.RARE),
    Animal("Dog", "🐶", Rarity.COMMON),
    Animal("Cat", "🐱", Rarity.COMMON),
    Animal("Rabbit", "🐰", Rarity.COMMON),
    Animal("Fox", "🦊", Rarity.COMMON),
    Animal("Bear", "🐻", Rarity.RARE),
    # Family Members
    Animal("Dad", "👨", Rarity.LEGENDARY, "/static/images/dad.png"),
    Animal("Mom", "👩", Rarity.LEGENDARY, "/static/images/mom.png"),
    Animal("Son", "👦", Rarity.LEGENDARY, "/static/images/son.png"),
    Animal("Grandpa", "👴", Rarity.LEGENDARY, "/static/images/grandpa.png"),
    Animal("Grandma", "👵", Rarity.LEGENDARY, "/static/images/grandma.png"),
]

class GameState:
    def __init__(self, total_boxes: int):
        self.total_boxes = total_boxes
        self.opened_boxes = 0
        self.boxes: Dict[int, Animal] = {} # Map box_index to Animal (once opened)

    def open_box(self) -> Optional[Dict]:
        if self.opened_boxes >= self.total_boxes:
            return None
        
        # Simple logic: Generate result on the fly for the next box
        # In a real "box" metaphor, we might pre-fill, but this is "Lucky Box"
        # so random on open is fine and simpler.
        
        # Weighted random choice based on rarity could be added here
        # For now, uniform random from the list
        animal = random.choice(ANIMALS)
        
        self.opened_boxes += 1
        box_index = self.opened_boxes # 1-based index
        
        self.boxes[box_index] = animal
        
        return {
            "box_index": box_index,
            "animal_name": animal.name,
            "emoji": animal.emoji,
            "rarity": animal.rarity.value,
            "image_url": animal.image_url
        }
