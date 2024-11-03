import os

def read_files_from_root():
    try:
        if os.name == 'nt':
            files = os.listdir('C:/')
        else:
            files = os.listdir('/')
        
        print("Files in root directory:")
        for file in files:
            print(file)
        
        with open('ayho.txt', 'w') as f:
            f.write("This is a test file.")
            
    except FileNotFoundError:
        print("File not found. You may not have permission to access this directory.")
    except PermissionError:
        print("PermissionError: You do not have permission to add files in this directory.")

read_files_from_root()



# Bonus: I would need root permissions (sudo) to write to the root directory on macOS/Linux/Unix.
