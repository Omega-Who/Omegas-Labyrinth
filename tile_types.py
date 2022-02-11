from math import floor
from typing import Tuple

import numpy as np # type: ignore


graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)
#  Tile graphics sturctured type compatible with Console.tiles_rgb.
#  d.type creates a data type which Numpy uses in a similar behaviour to "struct" in C. 
#  The data types used that are being used ar the following,
#  "ch" for the character represented in an integer format. Being translated into Unicode from an integer.
#  "fg" representing the foreground color. The "3B" gives us an unsigned 3 bytes to use for RGB colors as mentioned on the same code line.
#  Same goes for "bg" instead this time the background color.

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in the FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int,], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)
#  This helper function provides the help needed to define the tile types it takes the 3 parameters and it creates a Numpy array of just the one tile_dt element and returns it.

# SHROUD represents the undexplored, unseen tiles.
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)
wall = new_tile(
    walkable=False,
    transparent=False, 
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)),
)