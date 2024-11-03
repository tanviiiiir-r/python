class Car:
    def __init__(self, reg_number, make):
        self.reg_number = reg_number
        self.make = make

    def __str__(self):
        return f"{self.make} ({self.reg_number})"

cars = [
    Car("FIN-123", "Skoda"),
    Car("FIN-789", "Audi"),
    Car("FIN-456", "BMW"),
    Car("FIN-321", "Ford"),
    Car("FIN-654", "Opel"),
    Car("FIN-987", "Toyota"),
    Car("FIN-147", "Honda"),
    Car("FIN-258", "Mazda"),
    Car("FIN-369", "Nissan"),
    Car("FIN-741", "Volkswagen")
]

cars_sorted_by_make = sorted(cars, key=lambda car: car.make)
print("\nCars sorted by make:")
for car in cars_sorted_by_make:
    print(car)

cars_sorted_by_reg = sorted(cars, key=lambda car: car.reg_number)
print("\nCars sorted by registration number:")
for car in cars_sorted_by_reg:
    print(car)
