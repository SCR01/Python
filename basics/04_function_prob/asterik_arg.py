def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

#print(sum_all(1, 2, 3, 4, 5))
print(sum_all(10, 20, 30))

#aestrik argument example
def lol(*sharad):
    return sum(sharad)

print(lol(5))
    
    