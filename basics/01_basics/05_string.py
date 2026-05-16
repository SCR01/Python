chai = "lemon chai"
print(chai)
print(chai[0])

chai_slice = chai[0:5]
print(chai_slice)
num_lost = "0123456789"
print(num_lost[0:10:2])
print(num_lost[:])
print(num_lost[:7])
print(num_lost[3:])

some = "masala chai"
print(some.strip())
print(some.upper())

chai = "lemon, chai, masala"
print(chai.split(', '))

chai_variety = ["lemon", "masala", "ginger", "cardamom"]
print(', '.join(chai_variety))
print(' = '.join(chai_variety))

print(len(chai))
for letter in chai:
    print(letter)


print("Masala" in chai)