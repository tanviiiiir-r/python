def cel_2_fah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 1)

def fah_2_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 1)


print(cel_2_fah(10.0))  
print(fah_2_cel(50.0))  
