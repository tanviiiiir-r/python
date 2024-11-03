def count_names_in_file():
    try:
        with open("names.txt", "r") as file:
            names = file.read().splitlines()
        
        name_count = {}
        for name in names:
            name_count[name] = name_count.get(name, 0) + 1
        
        sorted_names = sorted(name_count.items())
        print("Number of names:", len(names))
        for name, count in sorted_names:
            print(f"{name}: {count}")
    except FileNotFoundError:
        print("File 'names.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_names_in_file()
