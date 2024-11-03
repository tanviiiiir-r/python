def isthiszero(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Parameter is not a number.")
    return num == 0

def check_isthiszero():
    test_values = [0, 5, -3, "string", None]
    for value in test_values:
        try:
            result = isthiszero(value)
            print(f"{value}: {result}")
        except TypeError as e:
            print(e)

check_isthiszero()
