import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_working_directory = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(abs_working_directory, file_path))
    valid_target_file = os.path.commonpath([abs_working_directory, target_file]) == abs_working_directory
    
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