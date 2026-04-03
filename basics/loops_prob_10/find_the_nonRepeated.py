scr = "sharad chandr areddy"

for char in scr:
    print(char)
    if scr.count(char) == 1:
        print("char is:",char)
        #break uss it only for the first non repeated character, if we want to find all non repeated characters then we should not use break statement