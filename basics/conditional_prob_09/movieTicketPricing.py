def movie(ticket_price):
    if ticket_price == '$10':
        return "adult"
    elif ticket_price == '$7':
        return "child"
    else:
        return "senior citizen"

print(movie('$10'))
print(movie('$7'))
print(movie('$5'))

day = "Monday"

if day == "Monday":
    print("Go to work and ticket price is $1")
else:
    print("Go to work and ticket price is same as before")