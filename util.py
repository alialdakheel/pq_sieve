
'''
From: https://stackoverflow.com/questions/2489435/check-if-a-number-is-a-perfect-square/45724520
'''
def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True
