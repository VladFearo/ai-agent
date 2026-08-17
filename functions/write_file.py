import os
from path_utils import resolve_path

def write_file(working_directory: str, file_path: str, content: str) -> str:
    target_file, valid_target_file = resolve_path(working_directory, file_path)
    
    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Could not write to file "{file_path}". Exception: {str(e)}'