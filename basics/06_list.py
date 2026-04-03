tea_variety = ["lemon", "masala", "ginger", "cardamom"]

print(tea_variety)
print(tea_variety[0])
print(tea_variety[-1])

print(tea_variety[1:3])
print(tea_variety[1:])
print(tea_variety[:3])

tea_variety.append("mint")
print(tea_variety)
tea_variety.insert(2, "tulsi")
print(tea_variety)
tea_variety.remove("masala")
print(tea_variety)
tea_variety[1:3] = ["chocolate", "strawberry"]
print(tea_variety)

for tea in tea_variety:
    print(tea)



if "Oolong" in tea_variety:
    print("Oolong is in the list")
else:    print("Oolong is not in the list")


tea_variety.extend(["peppermint", "chamomile"])
print(tea_variety)



newex = [x**2 for x in range(1,100)]
print(newex)