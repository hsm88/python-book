## OS_Code
import os

def organize_files(path):
    contents = os.listdir(path)

    list_of_files = []
    for item in contents:
        file_path = os.path.join(path, item)
        if os.path.isfile(file_path):
            list_of_files.append(item)

    set_of_file_extensions = set()
    for file in list_of_files:
        _, file_extension = os.path.splitext(file)
        set_of_file_extensions.add(file_extension)

    for extension in set_of_file_extensions:
        try:
            dir_path = os.path.join(path, extension[1:])
            os.mkdir(dir_path)
        except:
            continue

    for file in list_of_files:
        try:
            old_file_path = os.path.join(path, file)
            _, file_extension = os.path.splitext(file)
            new_file_path = os.path.join(path, file_extension[1:], file)
            os.rename(old_file_path, new_file_path)
        except:
            continue

    
organize_files(r"d:\python\examples\files")
