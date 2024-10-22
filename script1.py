""""Calculate the number of days since Ulam's birthday"""

from datetime import date


print('Hello word')

ulams_birthdate = date(1909, 4, 14)
ulam_days = (date.today() - ulams_birthdate).days

print("Number of days since Ulam's birthady: " , (date.today() - ulams_birthdate).days)

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

birthdate = date(year, month, day)
your_age = date.today() - birthdate


print(f'Ulam was {ulam_days - your_age.days} days old when you were born')
