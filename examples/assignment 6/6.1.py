def time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{remaining_seconds:02}"

test_values = [10000, 3661, 7325, 45296, 59]
for value in test_values:
    print(f"{value} seconds → {time(value)}")
