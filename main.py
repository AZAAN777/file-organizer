import os
import shutil


def organize_by_type(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            # Handle no extension and hidden files
            if filename.startswith('.'):
                ext = 'HIDDEN'
            elif '.' in filename:
                ext = filename.split('.')[-1]
            else:
                ext = 'NO_EXTENSION'

            target_dir = os.path.join(folder_path, ext.upper())
            os.makedirs(target_dir, exist_ok=True)

            new_path = os.path.join(target_dir, filename)

            # Skip if duplicate of the file exists
            if os.path.exists(new_path):
                print(f"Skipped duplicate: {filename}")
                continue

            shutil.move(full_path, new_path)
            print(f"Moved {filename} -> {target_dir}")


if __name__ == "__main__":
    folder_path = input("Enter the full folder path to organize: ")
    if os.path.exists(folder_path):
        organize_by_type(folder_path)
        print("Organization complete!")
    else:
        print("Invalid folder path.")
