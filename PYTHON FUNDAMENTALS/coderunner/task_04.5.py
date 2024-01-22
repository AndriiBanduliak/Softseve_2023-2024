def makes10(num1, num2):
  checkNum1 = num1 == 10 or num2 == 10
  checkSum = num1 + num2 == 10
  if checkNum1 or checkSum:
    return True
  else:
    return False
