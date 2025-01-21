def deposit():
    items = []
    while True:
        item = yield items
        items.append(item)

des = deposit()
print(next(des)) # inicia o gerador

print(des.send("smogon"))
print(des.send("smogon"))

