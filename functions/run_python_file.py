from path_utils import resolve_path


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    target_file, valid_target_file = resolve_path(working_directory, file_path)
