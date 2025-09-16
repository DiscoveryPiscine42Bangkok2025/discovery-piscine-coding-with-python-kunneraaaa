first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
answer = first_number * second_number
print(f"{first_number} x {second_number} = {answer}")
if answer > 0:
    print("The result is positive.")
elif answer < 0:
    print("The result is negative.")
elif answer == 0:
    print("The result is positive and negative.")