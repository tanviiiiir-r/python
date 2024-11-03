def modify_collection():
    strings = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    while True:
        try:
            index = int(input("Enter index to modify (0-4): "))
            if index < 0 or index >= len(strings):
                raise IndexError("Invalid index.")
            new_text = input("Enter new text: ")
            strings[index] = new_text
            break
        except IndexError as e:
            print(e)
        except ValueError:
            print("Please enter a valid integer.")

    print("Updated collection:")
    print(strings)

modify_collection()
