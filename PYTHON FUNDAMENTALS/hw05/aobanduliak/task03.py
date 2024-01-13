def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example usage
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
