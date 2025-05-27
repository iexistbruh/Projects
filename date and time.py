from datetime import date, datetime

today=date.today()
now=datetime.now()
print("today's date is ", today)
print("\ncurrent date and time is ",now)

print("\nDate components", today.year,today.month,today.day)