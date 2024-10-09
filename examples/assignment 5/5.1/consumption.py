from utils import calc_consumption

consumption_per_100km = float(input("Enter the vehicle's fuel consumption (liters per 100km): "))
fuel_price = float(input("Enter the fuel price per liter: "))
distance = float(input("Enter the traveled distance in kilometers: "))

calc_consumption(consumption_per_100km, fuel_price, distance)
