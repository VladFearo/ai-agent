import os
from path_utils import resolve_path

def get_files_info(working_directory: str, directory: str = ".") -> str:
    target_dir, valid_target_dir = resolve_path(working_directory, directory)


    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{target_dir}" is not a directory'
    else: 
        dir_list = os.listdir(target_dir)
        str_list = []
        for file in dir_list:
            name = file
            file_size = os.path.getsize(os.path.join(target_dir, file))
            is_dir = os.path.isdir(os.path.join(target_dir, file))
            str_list.append(f'- {name}: file_size={file_size} bytes, is_dir={is_dir}')
        return "\n".join(str_list)