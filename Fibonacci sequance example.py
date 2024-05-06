def fibonacci(n):
    if n <= 0:
        return "Invalid Input"
    
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else: fib_sequence = [0, 1]

    for i in range(2, n):

        fib_sequence.append(fib_sequence[-1] +
        fib_sequence[-2])
        return fib_sequence[-1]
    
    print(fibonacci(7))