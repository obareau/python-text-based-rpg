from .. import item

@property
def consumable_items(player):
    return [
        inventory_item
        for inventory_item in player.inventory
        if inventory_item.type == item.CONSUMABLE
    ]
"""property: A property that computes a list of the items the player has in
their inventory which are consumable."""

@property
def equippable_items(player):
    return [
        inventory_item
        for inventory_item in player.inventory
        if inventory_item.type == item.EQUIPPABLE
    ]
"""property: A property that computes a list of the items the player has in
their inventory which are equippable."""
