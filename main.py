"""
Given a String as input, remove all digits from the string. Use recursion. Do not use loops. Do a dry run for each test case.
Input-> "x1Y2Z3qw#"
Output-> xYZqw#
"""

def removeDigi(st):
  ln = len(st)
  if (ln==0):
    return 0
  ch = st[0]
  if (ch>=0 and ch<=9):
    return 0
  else:
    return ch + removeDigi(st[1:])

st = "x1Y2Z3qw#"
print(removeDigi(st))