"""A regex to make sure the password string containing at least 8 char, both upper- and lower case and at least 1 digit"""
import re

valid_pass = "Ab12e45678"
invalid_pass_too_short = "Ab2"
invalid_pass_no_upper = "ab12e456"
invalid_pass_not_lower = "AB12E456"
invalid_pass_no_digit = "AbcdEfgHi"
invalid_pass_no_letter = "123456789"
regex = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}$')


def isValidPass(password):
    if re.match(regex, password):
        return True
    else:
        return False


print(isValidPass(valid_pass))
print(isValidPass(invalid_pass_too_short))
print(isValidPass(invalid_pass_no_upper))
print(isValidPass(invalid_pass_not_lower))
print(isValidPass(invalid_pass_no_digit))
print(isValidPass(invalid_pass_no_letter))

"""
?= is a lookahead assertion: http://www.regular-expressions.info/lookaround.html
. matches any character except a newline; 
in square brackets the . is limited to only what is defined in the []; 
also know as atomic grouping.
"""