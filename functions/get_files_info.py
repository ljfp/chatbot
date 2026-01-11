import os

def get_files_info(working_directory, directory="."):
    working_directory_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
    if not os.path.isdir(target_dir):
        return f'    Error: "{directory}" is not a directory'
    is_target_dir_valid = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
    if not is_target_dir_valid:
        return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
    contents = os.listdir(target_dir)
    summary = ""
    for item in contents:
        item_path = os.path.join(target_dir, item)
        size = None
        is_dir = None
        try:
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
        except Exception:
            print("    Error: Something went wrong when getting the file size or checking if it's a dir")
        summary += f"  - {item}: file_size={size} bytes, is_dir={is_dir}\n"
    return summary

