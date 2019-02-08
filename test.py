inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

loot = [('mleko', 10)]


print(inv.items())
inv.update(loot)
print(inv.items())