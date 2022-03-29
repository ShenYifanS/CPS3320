'''
Tutorial5
Yijie Zhang
Yifan Shen
'''

import re
string1 = "abb29ABCLK%lCnrDBCabbbb"

# .	Matches any character, except newlines
# $ Match the end of the string
# Finds all substrings in the string that the regular expression matches and returns a list
pattern = re.findall(".{5}$", string1)
print(pattern)

print(re.search("[A-Z][a-z]+", string1))
# String starting with an uppercase letter, followed by 1 or more lowercase letters
# output: <re.Match object; span=(12, 15), match='Cnr'>