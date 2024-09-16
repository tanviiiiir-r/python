n1 = int(input("enter fist integer: "))
n2 = int(input("enter second integer: "))
n3 = int(input("enter third integer: "))

large = n1

if n2 > large:
   large = n2
   
   if n3 > large:
      large = n3
      
print("The largest number is: ", large)