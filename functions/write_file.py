import os

def write_file(working_directory, file_path, content):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
    is_target_file_valid = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs
    if not is_target_file_valid:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    os.makedirs(working_directory, exist_ok=True)
    with open(target_file, "w") as f:
        try:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception:
            print(f"    Error: Couldn't write to {file_path}")
    return None

