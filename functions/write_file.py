import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a specified file inside the working directory.",
    parameters=types.Schema(
        required=["file_path", "content"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write content to, relative to the working directory"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content we are going to write into the file."
            )
        },
    ),
)

