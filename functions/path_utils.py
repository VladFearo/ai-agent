import os


def resolve_path(working_directory: str, path: str) -> tuple[str, bool]:
    abs_working_directory = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(abs_working_directory, path))

    is_valid = (
        os.path.commonpath([abs_working_directory, target_path])
        == abs_working_directory
    )

    return target_path, is_valid
