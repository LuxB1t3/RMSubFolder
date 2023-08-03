import os

def change_directory_names(path, old_name, new_name):
    for dirpath, dirnames, filenames in os.walk(path):
        for folder_name in dirnames:
            if folder_name == old_name:
                old_folder_path = os.path.join(dirpath, folder_name)
                new_folder_path = os.path.join(dirpath, new_name)
                os.rename(old_folder_path, new_folder_path)
                print(f"Changed: {old_folder_path} -> {new_folder_path}")

if __name__ == "__main__":
    base_folder_name = "RM" # Do not change this
    old_folder_name = "OLD-FOLDER-NAME"
    new_folder_name = "NEW-FOLDER-NAME"

    base_path = os.path.join(os.path.join(os.path.join(os.path.join("C:\\Users\\<USERNAME>"), 'Desktop'), 'RMSubFolder'), base_folder_name)

    change_directory_names(base_path, old_folder_name, new_folder_name)