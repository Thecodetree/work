def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def div(a, b):
   answer = a / b
   print(str(a) + "/" + str(b) + "=" + str(answer))

def mul(a, b):
   answer = a * b
   print(str(a) + "*" + str(b) + "=" + str(answer))
   
print ('A. addition')
print('B. Subtraction')
print('C. Division')
print('D. Multiplication')

choice = input('Input your choice: ')

if choice == 'a' or choice == 'A':
    print('Addition')
    a = int(input ('input your first number: '))
    b = int(input ('input your second number: '))
    add (a + b)

elif choice == 'b' or choice == 'B':
    print('Subtraction')
    a = int(input ('input your first number: '))
    b = int(input ('input your second number: '))
    sub (a - b)

elif choice == 'c' or choice == 'C':
    print('Division')
    a = int(input ('input your first number: '))
    b = int(input ('input your second number: '))
    div (a / b)
    
elif choice == 'd' or choice == 'D':
    print('Multiplication')
    a = int(input ('input your first number: '))
    b = int(input ('input your second number: '))
    mul (a * b)
elif choice == 'e' or choice == 'E':
    print('Program ended')
    quit()