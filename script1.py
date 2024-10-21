from datetime import date, timedelta


print('Hello word')

ulams_birthdate = date(1909, 4, 14)

print("Number of days since Ulam's birthady: " , (date.today() - ulams_birthdate).days)

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

bithdate = date(year, month, day)
your_age = date.today().day

ulam_days = (date.today() - ulams_birthdate)
print(f'Ulam was {ulam_days - your_age.day} days old when you were born')
