def separate_numbers_to_files():
    integers = []
    floats = []
    
    while True:
        user_input = input("Enter a number (integer or float), or anything else to stop: ")
        try:
            number = float(user_input)
            if number.is_integer():
                integers.append(int(number))
            else:
                floats.append(number)
        except ValueError:
            break

    try:
        with open("integers.txt", "w") as int_file:
            for integer in integers:
                int_file.write(f"{integer}\n")
        
        with open("floats.txt", "w") as float_file:
            for float_num in floats:
                float_file.write(f"{float_num}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

separate_numbers_to_files()
