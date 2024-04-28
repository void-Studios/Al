import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def format_size(size_bytes):
    # Convert bytes to gigabytes
    return "{:.2f} GB".format(size_bytes / (1024 ** 3))

def visualize_folders(folder_path):
    print(folder_path)
    print("Folder".ljust(30),"Size")
    print("-" * 40)
    for dir_name in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir_name)
        if os.path.isdir(dir_path):
            folder_size = get_folder_size(dir_path)
            print(f"{dir_name.ljust(30)} {format_size(folder_size)}")

if __name__ == "__main__":
    folder_path = input("Enter the directory path to visualize: ")
    visualize_folders(folder_path)
