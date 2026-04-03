
def person(age):
    if age<13:
        return "child"
    elif age>=13 and age<20:
        return "teenager"
    else:
        return "adult"
    
print(person(12))
print(person(15))