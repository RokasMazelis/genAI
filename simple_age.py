from datetime import datetime

year_input = input ("Iveskite gimimo metus")
month_input = input ("Iveskite gimimo menesi")
day_input = input ("Iveskite gimimo diena")

year = int(year_input)
month = int(month_input)
day = int(day_input)

current_date = datetime.now()


date_of_brith = datetime(year, month, day)

age = current_date - date_of_brith

print(age)

