"""
    Write a function that takes a string and does the same thing as the strip()
    string method. If no other arguments are passed other than the string to
    strip, then whitespace characters will be removed from the beginning and
    end of the string. Otherwise, the characters specified in the second argu-
    ment to the function will be removed from the string.
"""
import re

sample_str = " This is a sample String. "
regex = re.compile(r'^\s+|\s+$')


def regex_strip(s, char=None):
    if not char:
        s = regex.sub("", s)  # replacing space with "" in string s
    else:
        strip_char = re.compile(re.escape(char))
        s = re.sub(strip_char, "", s)
    return s


print(sample_str.strip())
print(regex_strip(sample_str))
print(sample_str.strip() == regex_strip(sample_str))
print(regex_strip(sample_str, 'is'))
