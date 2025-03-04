def recursive_multiply(a, b):
    a_str = str(a)
    b_str = str(b)
    if len(a_str) == 1 and len(b_str) == 1:
        return a * b

    n = max(len(a_str), len(b_str))
    m = n // 2

    # Divide
    high_a = a // (10**m)
    low_a = a % (10**m)
    high_b = b // (10**m)
    low_b = b % (10**m)

    # Conquer
    a1 = high_a + low_a
    b1 = high_b + low_b
    p = recursive_multiply(a1, b1)
    a1b1 = recursive_multiply(high_a, high_b)
    a0b0 = recursive_multiply(low_a, low_b)

    # Combine
    return a1b1 * (10**(2*m)) + (p - a1b1 - a0b0) * (10**m) + a0b0


def menu():
    while True:
        print("-Integer Multiplication Menu-")
        print("1. Multiply two integers")
        print("2. Exit")
        c = int(input("Enter your choice: "))

        if c == 1:
            a = int(input("Enter integer number 1: "))
            b = int(input("Enter integer number 2: "))
            result = recursive_multiply(a, b)
            print("The result of multiplication is", result)
        elif c == 2:
            print("Exiting...")
            break
        else:
            print("Enter a valid choice")


menu()
