from random import randint

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

cars = [car1, car2, car3]
total_price = sum(car.price for car in cars)

for i, car in enumerate(cars, 1):
    print(f"car{i}: {car.brand} {car.model} {car.price}")
print(f"Total price of the cars is {total_price}")

brands = ["Audi", "BMW", "Ford", "Opel", "Skoda", "Volvo", "VW"]
random_cars = []

for _ in range(5):
    brand = brands[randint(0, len(brands) - 1)]
    model = ""
    price = randint(1000, 10000)
    random_cars.append(Car(brand, model, price))

for i, car in enumerate(random_cars, 1):
    print(f"Random car{i}: {car.brand} {car.model} {car.price}")
