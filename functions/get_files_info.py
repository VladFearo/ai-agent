import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_directory, directory))
    
    valid_target_dir = os.path.commonpath([abs_working_directory, target_dir]) == abs_working_directory
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{target_dir}" is not a directory'
    else: 
        return f'Success: "{target_dir}" is within the working directory'
