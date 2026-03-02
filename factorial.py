# Program to calculate factorial of 5 numbers

for i in range(5):
    num = int(input("Enter a number: "))
    factorial = 1

    if num < 0:
        print("Factorial does not exist for negative numbers ❌")
    else:
        for j in range(1, num + 1):
            factorial *= j
        print(f"Factorial of {num} is {factorial} ✅\n")
