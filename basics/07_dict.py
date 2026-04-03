ex1 = {'a': 1, 'b': 2, 'c': 3}
print(ex1.get('a'))

ex1['c'] = 4
print(ex1)

for iterm in ex1:
    print(iterm)

for key in ex1:
    print(key, ex1[key])

for key, value in ex1.items():
    print(key, value)


del ex1['b']
print(ex1)

print(ex1.pop('a'))

print(ex1)
ex1['d', 'e'] = 5, 6
print(ex1)
print(len(ex1))

ex1_copy = ex1.copy()
print(ex1_copy)

tea_shop = {
    "chai":{"masala": 10, "lemon": 8, "ginger": 9},
    "coffee":{"black": 12, "white": 15, "cold": 10}
}

print(tea_shop['chai']['lemon'])
print(tea_shop['coffee']['white'])
print(tea_shop['chai'])
print(tea_shop['coffee'])

squares = {x:x**2 for x in range(1,11)}
print(squares)
print(squares.clear())

keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)