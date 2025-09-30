def factorial(n: int) -> int:
    """Return factorial of n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")
