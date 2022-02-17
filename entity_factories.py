from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=3),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=100),
)

# Enemies

goblin = Actor(
    char="g",
    color=(34, 139, 34),
    name="Goblin",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=5, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=10),
)

hobgoblin = Actor(
    char="H",
    color=(0, 128, 0),
    name="Hobgoblin",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=8, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)

troll = Actor(
    char="T",
    color=(0, 100, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

# Miniboss(es)

goblin_king = Actor(
    char="K",
    color=(53, 94, 59),
    name="Goblin King",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=24, base_defense=2, base_power=6),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=200),
)

minotaur = Actor(
    char="M",
    color=(225, 193, 110),
    name="Minotaur",
    ai_cls=HostileEnemy,
    equipment=Equipment(equippable.Sword),
    fighter=Fighter(hp=24, base_defense=3, base_power=7),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=250),
)

"""Insert Them here at some point."""

# Items

confusion_scroll = Item(
    char="$",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="$",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)

health_potion = Item(
    char="$",
    color=(0, 150, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)

elixir = Item(
    char="$",
    color=(128, 0, 128),
    name=("Elixir"),
    consumable=consumable.ElixirConsumable(amount=8)
)

lightning_scroll = Item(
    char="$",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="-", 
    color=(0, 191, 255), 
    name="Dagger", 
    equippable=equippable.Dagger(),
)

sword = Item(
    char="-", 
    color=(0, 191, 255), 
    name="Sword", 
    equippable=equippable.Sword(),
)

leather_armor = Item(
    char="~",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="~",
    color=(139, 69, 19),
    name="Chain Mail",
    equippable=equippable.ChainMail()
)