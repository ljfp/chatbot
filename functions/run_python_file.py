import os
import subprocess
from typing import Required
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
    is_target_file_valid = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs
    if not is_target_file_valid:
        return f'    Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'    Error: "{file_path}" does not exist or is not a regular file'
    if file_path[-3:] != ".py":
        return f'    Error: "{file_path}" is not a Python file'
    command = ["python", target_file]
    if args:
        command.extend(args)
    try:
        completed_process = subprocess.run(
            command,
            cwd=working_directory_abs,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )
    except Exception:
        return f"Error: executing Python file: {file_path}"
    result = ""
    return_code = completed_process.returncode
    stdout = completed_process.stdout
    stderr = completed_process.stderr
    if return_code != 0:
        result += f"Process exited with code {return_code}\n"
    if (not stdout) and (not stderr):
        result += "No output produced\n"
    else:
        result += f"STDOUT: {stdout}\n"
        result += f"STDERR: {stderr}\n"
    return result

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute the python file provided in file_path, with the arguments provided in args.",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file we are going to execute"
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of arguments to provide to the file we are about to execute",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)

