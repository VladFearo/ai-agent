from functions.path_utils import resolve_path
import os, subprocess


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file relative to the working directory with optional command-line arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path of the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Optional command-line arguments to pass to the Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        target_file, valid_target_file = resolve_path(working_directory, file_path)
        abs_working_directory = os.path.abspath(working_directory)

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args:
            command.extend(args)

        complete = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=abs_working_directory,
            timeout=30
        )

        output_string = ""

        if complete.returncode != 0:
            output_string += f'Process exited with code {complete.returncode}\n'

        if not complete.stdout and not complete.stderr:
            output_string += 'No output produced\n'
        else:
            if complete.stdout:
                output_string += f'STDOUT: {complete.stdout}\n'
            if complete.stderr:
                output_string += f'STDERR: {complete.stderr}\n'

        return output_string

    except Exception as e:
        return f"Error: executing Python file: {e}"