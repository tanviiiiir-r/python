sum = 0

for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    if num > 0:
        sum += num

print("The sum of the positive numbers is:", sum)
