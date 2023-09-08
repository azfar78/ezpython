def main():
    try:
        # Step 1: Prompt the user to enter the first number
        num1 = float(input("Enter the first number: "))

        # Step 2: Prompt the user to enter the second number
        num2 = float(input("Enter the second number: "))

        # Step 3: Calculate the sum of the two numbers
        result = num1 + num2

        # Step 4: Display the result to the user
        print("The sum of", num1, "and", num2, "is:", result)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
