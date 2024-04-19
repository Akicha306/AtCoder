import os

def rename_files(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Sort the files in ascending order
    files.sort()

    # Iterate over the files and rename them
    for i, file_name in enumerate(files):
        # Construct the new file name with the specified number
        new_file_name = f"No.{i+1}"

        # Get the full path of the file
        file_path = os.path.join(folder_path, file_name)

        # Get the full path of the new file
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(file_path, new_file_path)

        print(f"Renamed {file_name} to {new_file_name}")

# Specify the folder path
folder_path = os.path.dirname(os.path.abspath(__file__))
start= 171
end = 172
folder_path = 

# Call the function to rename the files
rename_files(folder_path)