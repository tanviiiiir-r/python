p = int(input("Enter the number of point: "))

if 0 <= p <= 1:
    g = 0
elif 2 <= p <= 3:
    g = 1
elif 4 <= p <= 5:
    g = 2
elif 6 <= p <= 7:
    g = 3
elif 8 <= p <= 9:
    g = 4
elif 10 <= p <= 12:
    g = 5
else:
    g = "Invalid input"

print("The grade is:", g)
