def leap_year_checker(year):
    if year%4==0 and year%100 !=0 or year%400==0:
        return "leap year"
    else:        return "not a leap year"

print(leap_year_checker(2020))
print(leap_year_checker(1900))