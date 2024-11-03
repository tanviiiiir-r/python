def write_last_names_to_file():
    last_names = []
    while True:
        name = input("Enter last name (or press Enter to finish): ")
        if name == "":
            break
        last_names.append(name)

    try:
        with open("last_names.txt", "w") as file:
            for name in last_names:
                file.write(name + "\n")
        
        print("Last names written to file. Contents of the file:")
        with open("last_names.txt", "r") as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"An error occurred: {e}")

write_last_names_to_file()

