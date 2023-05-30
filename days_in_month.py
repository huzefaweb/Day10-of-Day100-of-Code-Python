def is_leap(year):
  '''this function check if a specific year if leap year or not'''
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap_year = True
      else:
        leap_year = False
    else:
      leap_year = True
  else:
    leap_year = False
  return leap_year

def day_month(month, year):
  if month > 12 or month < 1:
    return "Invalid Month"
  leapyear = is_leap(year)
  if leapyear == True:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]
  else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]

year = int(input("enter the year: "))
month = int(input("enter the month to know the days in that month: "))

days = day_month(month, year)
print(days)
