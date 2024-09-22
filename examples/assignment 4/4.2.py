import random

def lottery():

    return random.sample(range(1, 41), 7)

def main():

    num_sets = int(input("How many lottery sets would you like to generate? "))
    
    for i in range(num_sets):
        numbers = lottery()
        print(f"Lottery set {i + 1}: {sorted(numbers)}")

if __name__ == "__main__":
    main()
