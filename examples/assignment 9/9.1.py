def change_value_in_list():
    my_list = [1, 2, 3, 4]
    try:
        my_list[4] = 5
    except IndexError:
        print("IndexError: Tried to access an index that does not exist.")

change_value_in_list()
