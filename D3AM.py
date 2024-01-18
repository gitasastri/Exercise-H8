#Day 3 AM - Python: Conditions and Loops

#Exercise 1
n = 9 
for i in range(0, n):
    for j in range(0, i+1):
        print("1", end=" ")
    print()

print('\n')

#Exercise 2
#Write a python program to check the validity of password input by users 
def isContainLowerUpperNumber(password):
  isContainLower = False
  isContainerUpper = False
  isContainNumber = False
  isContainSymbol = False

  for char in [*password]:
    if char.islower():
      isContainLower = True

    if char.isupper():
      isContainerUpper = True

    if char.isdigit():
      isContainNumber = True

    if char in ['$', '#', '@']:
      isContainSymbol = True


  if(isContainLower and isContainerUpper and isContainNumber and isContainSymbol and len(password) >= 6 and len(password) <= 16):
    return None
  else:
    message = []
    if not(isContainLower):
      message.append('Harus mengandung a-z')

    if not(isContainerUpper):
      message.append('Harus mengandung A-Z')

    if not(isContainNumber):
      message.append('Harus mengandung 0-9')

    if not(isContainSymbol):
      message.append('Harus mengandung [$#@]')
    return 'Password is Invalid ' + ', '.join(message)

password = input('Silahkan input password: ')
message = isContainLowerUpperNumber(password)
print(message)
