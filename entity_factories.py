from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(215, 112, 126), 
    name="Player", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

orc = Actor(
    char="o", 
    color=(63, 127, 63), 
    name="Orc", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)
troll = Actor(
    char="T", 
    color=(0, 127, 0),
    name="Troll", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)
