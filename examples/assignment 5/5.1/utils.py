def show_info():
    
    print("I'm Utils.Info")

def subtract(a, b):

    return a - b

def average(x, y, z):

    return round((x + y + z) / 3, 1)


def calc_consumption(consumption_per_100km, fuel_price, distance):
    liters_used = (consumption_per_100km / 100) * distance
    cost = liters_used * fuel_price
    print(f"Fuel used: {liters_used:.2f} liters")
    print(f"Cost of fuel: {cost:.2f} currency units")