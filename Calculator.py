A = int(input('Enter first number (1-1000000):  '))
B = int(input('Enter second number (1-1000000): '))

operator = input('Enter which operator you want to use (+ - * / % **):  ')

if operator == '+':
  Answer = A + B
elif operator == '-':
  Answer = A - B
elif operator == '*':
  Answer = A * B
elif operator == '/':
  if B == 0:
    print('Cannot divide by zero')
  else:
      Answer = A / B
elif operator == '%':
  Answer = A % B
elif operator == '**':
  Answer = A ** B
else:
  print('Wrong input')

if 'Answer' in locals():
  print(Answer)