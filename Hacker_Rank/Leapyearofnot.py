'''if year%4 == 0 and year%400 == 0:
  print('True')
if year%100 == 0:
  print('False')
else:
  print('False')'''

def is_leap(year):
  if year%4 == 0:
    return True
  if year%100 == 0:
    return False
  if year%400 == 0:
    return True

year = int(input())
print(is_leap(year))