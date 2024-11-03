class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

human1 = Human("Tanvir", 18)
human2 = Human("ovi", 20)

print(human1)
print(human2)
