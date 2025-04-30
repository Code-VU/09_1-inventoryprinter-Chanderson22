stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    print("Inventory:")
    for items in inventory:
        print(inventory[items], items)
if __name__ == "__main__":
    displayInventory(stuff)
