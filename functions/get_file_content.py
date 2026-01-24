from config import MAX_CHARS
from google.genai import types
import os

def get_file_content(working_directory, file_path):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
    is_target_file_valid = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs
    if not is_target_file_valid:
        return f'    Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'    Error: File not found or is not a regular file: "{file_path}"'
    content = ""
    with open(target_file, "r") as f:
        try:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        except Exception:
            print("    Error: Couldn't read file")
    return content

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieve the content of a file, up to {MAX_CHARS}. The file must be located in the working directory.",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to list the contents from, relative to the working directory."
            ),
        },
    ),
)

