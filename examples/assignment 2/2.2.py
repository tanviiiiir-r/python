n1 = int(input("Enter the first integer="))
n2 = int(input("Enter the second integer="))

sum_result = n1 + n2
subtraction_result = n1 - n2
multiplication_result = n1 * n2

if n2 !=0:
    division_result = n1 / n2

else:
    divison_result = "undefined (second number can not be zero)"

print("Sum:", sum_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)

