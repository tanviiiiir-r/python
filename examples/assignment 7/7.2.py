class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.name} says: Meoooooow!")

cat1 = Cat("Kitty", "black")
cat2 = Cat("pusy kat", "white")

print(f"{cat1.name}, Color: {cat1.color}")
print(f"{cat2.name}, Color: {cat2.color}")
cat1.meow()
cat2.meow()
