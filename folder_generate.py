import os

start_num = int(input("Enter start number: "))
end_num = int(input("Enter end number: "))

def create_folders(start_num, end_num, directory):
    """
    This function creates folders with numbered names between start_num and end_num in the specified directory.
    """
    for i in range(start_num, end_num):
        folder_name = str(i*7)
        folder_path = os.path.join(directory, folder_name)
        try:
            os.mkdir(folder_path)
            print(f"Folder {folder_name} created successfully!")
        except FileExistsError:
            print(f"Folder {folder_name} already exists!")

create_folders(start_num, end_num, "./")