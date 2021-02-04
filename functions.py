#---------------------------------------------------------------calc
# calculator app
# two number inputs (a,b)
# methods: addition, subtraction, multiplication, division
# test cases
def calc(a, b, c):
  if(type(a) not in [int, float] || type(b) not in [int, float]):
    raise TypeError('Input must be int or float')
  if(type(c) not in [str]):
    raise TypeError('Opperator must be string')

  if(c == '+'):
    return a+b

  elif(c == '-'):
    return a-b

  elif(c == '*'):
    return a*b

  elif(c == '/'):
    if(b == 0):
      return 0
    return a/b

  else:
    raise TypeError('Undefined opperator')
