def ski_jumping_score():
    points = []
    
    for i in range(1, 6):
        point = int(input(f"Give points from judge {i}: "))
        points.append(point)
    
    total_points = sum(points) - min(points) - max(points)
    print(f"Total points are: {total_points}")

ski_jumping_score()
