def password_checker(password):
    if len(password) < 8:
        return "Password is too short"
    elif len(password) > 20:
        return "password is too long"
    elif not any(char.isdigit()for char in password):
        return "Password should contain at least one digit"
    elif not any(upper.isupper() for upper in password):
        return "Password should contain at least one uppercase letter"
    else:
        return "Password is strong"
    
print(password_checker("IndiaCitizen@1"))