# def remove(string):
# 	return "".join(string.split())
# string = 'P R A T E E K'
# print(remove(string))

import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")