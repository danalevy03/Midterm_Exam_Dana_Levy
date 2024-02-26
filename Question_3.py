import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week #7 + 0 = 7
b += month_of_year #2 + 2 = 4

print(a)
print(b)
c = a + b #7 + 4 = 11
print(c)
d = "xyz" * (c // 3)  # "xyz" * (11 // 3) = "xyz" * 3 = "xyzxyzxyz"
print(d)

