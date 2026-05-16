

# this is comment

#object types / data types

#Number: 1234, 3.1414, 3+4j, 0b111, decimal(), fraction()

#String: 'spam;, "Bob's", b'a\x01c', u'sp\xc4m'

#list : [1,[2,'three'], 4.5], list(range(20))

#Tuple: (1,'spam', 4,'U'), tuple('spam'), namedtuple

#Dictionary: {'food': 'spam', 'taste':'yum'}, dict(hours=10)

#Set: set('abc'), {'a', 'b', 'c'} //unique values

#Boolean: True, False
#None: None

#Functions, modules, classes

#Advance: Decorators, Generators, Iterators, Metaprpogramming, Context Managers, Coroutines, Asyncio

mylist = [1,2,['a','b'], 3.5]
print(mylist)
print(len(mylist))


lol = None
print(lol)


import math
print(math.pi)

username = "chaiaurcode"
len(username)

print(username)

print(username[0])
print(username[-1])


myD = {'name': 'chaiaurcode', 'age': 1, 'course': 'python'}
print(myD)
print(myD['name'])
print(myD['age'])
print(myD['course'])


myListone = [1,2,3,4,5]
mylistone = myListone
print(myListone)
mylistone[0] = 100
print(myListone)