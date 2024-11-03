def collect_student_names():
    student_names = []
    
    while True:
        name = input("Enter student name: ").strip()
        if not name:
            break
        student_names.append(name)
    
    print(f"Student count: {len(student_names)}")
    print(",".join(student_names))

collect_student_names()
