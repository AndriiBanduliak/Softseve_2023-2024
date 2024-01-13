def print_fibonacci_up_to_n(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b


# Example usage
n = int(input("Enter a number: "))
print_fibonacci_up_to_n(n)
