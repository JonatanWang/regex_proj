"""A regular expression that can detect dates in the DD/MM/YYYY format."""
import re
import pyinputplus as pyip

input_str = pyip.inputStr(prompt="Please input a string, containing a date: ", default='Today is 15/04/2020.')

date_regex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-9]+[0-9]*)')
date_object = date_regex.search(input_str)  # Example: "Today is 15/04/2020."
print(f'Readin object -> {date_object}')

day = date_object.group(1)
month = date_object.group(2)
year = date_object.group(3)
print(f'Readin -> Day: {day} Month: {month} Year: {year}')


def isLeapYear():
    formatted_year = int(year)
    return (formatted_year % 4 == 0 and not formatted_year % 100 == 0) \
           or (formatted_year % 4 == 0 and formatted_year % 400 == 0 and not formatted_year % 100 == 0)


def isValidDay():
    formatted_day = int(day)
    formatted_month = int(month)
    if not 1 <= formatted_day <= 31:
        return False
    if formatted_month in [4, 6, 9, 11] and formatted_day > 30:
        return False
    if not isLeapYear() and formatted_month == 2 and formatted_day > 28:
        return False
    if formatted_month == 2 and formatted_day > 29:
        return False
    return True


def isValidMonth():
    return 1 <= int(month) <= 12


def isValidYear():
    return int(year) >= 1


def isValidDate():
    return isValidDay() and isValidMonth() and isLeapYear()


if isValidDate():
    print(f'Day: {day} Month: {month} Year: {year}')
else:
    print("It is not a valid date.")
