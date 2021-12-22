import os


def is_file_name_needs_change(name):
    result = " " in name or "-" in name
    return result


def format_file_name(name):
    return name.replace(" ", "_").replace("-", "_")


def rename_file(filename):
    if is_file_name_needs_change(filename):
        new_name = format_file_name(filename)
        print(f"New Name is = {new_name}")
    else:
        print("No need to change file name")


folder_name = "/"
files = os.listdir(folder_name)

for count, filename in enumerate(files):
    if os.path.isfile(filename):
        rename_file(filename)



