while True:
    user_input = int(input("Enter a number: btw 1 and 10: 2"))
    if 1<= user_input <= 10:
        print("valid input")
        break 
    else:
        print("invalid input, try again")
