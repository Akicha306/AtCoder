import os

def make_folders(start, end):
    folder_path = os.path.dirname(os.path.abspath(__file__))
    for i in range(start, end+1):
        folder_name = "No."+str(i)
        folder_dir = os.path.join(folder_path, folder_name)
        os.makedirs(folder_dir, exist_ok=True)
        print(f"Created folder: {folder_dir}")

# Specify the starting and ending numbers for the folders
start_number = 1
end_number = 2

make_folders(start_number, end_number)