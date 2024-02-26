#Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how many days have passed since your birthday (without counting the days in your birth year and the current year, so just whole years).
#The function takes your birthday as a parameter in string format.
# Do not import anything

def days_passed_since_dana_was_born(birthday):
    birth_day, birth_month, birth_year = birthday.split("-") #splitting the birthday into day, month and year
    today = current_month, current_day, current_year = "26-02-2024".split("-") #today's date
    days_passed = 0
    for year in range(int(birth_year) + 1, int(current_year)): #looping through the years between the birth year and the current year
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: #checking if the year is a leap year
            days_passed += 366
        else:
            days_passed += 365

    if int(birth_month) == 2 and int(birth_day) == 29: #checking if the birth month is February and the birth day is 29
        days_passed -= 1
    return days_passed

print(days_passed_since_dana_was_born("01-06-2003"))
# 7305 is the answer




