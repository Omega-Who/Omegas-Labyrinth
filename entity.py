from __future__ import annotations

import copy
from typing import Optional, Tuple, Type, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from components.ai import BaseAI
    from components.fighter import Fighter
    from game_map import GameMap

T = TypeVar("T", bound="Entity")


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    gamemap: GameMap

    def __init__(
        self,
        gamemap: Optional[GameMap] = None,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        blocks_movement: bool = False,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            # If gamemap isn't provided now then it will be set later.
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location. Handles moving across GameMaps."""
        self.x = x 
        self.y = y 
        if gamemap:
            if hasattr(self, "gamemap"):  # Possibly uninitialized.
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

class Actor(Entity):
    def __init__(
        self,
        *,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        ai_cls: Type[BaseAI],
        fighter: Fighter
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            blocks_movement=True,
        )

        self.ai: Optional[BaseAI] = ai_cls(self)

        self.fighter = fighter
        self.fighter.entity = self

    @property
    def is_alive(self) -> bool:
        """Retuurns True as long as this actor rcan nperform actions."""
        return bool(self.ai)