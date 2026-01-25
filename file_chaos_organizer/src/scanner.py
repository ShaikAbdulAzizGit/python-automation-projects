from pathlib import Path

def scan_directory(source_path:Path,recursive:bool=False)->list[Path]:
    '''
    Scans source directory and returns list of file paths

    Args:
        source_path(Path): Path to the directory for which file organization will be performed
        recursive(bool): Whether to scan sub directories (True/False)

    Returns: 
        files(List[path]): list of paths for files in source directory 

    Raises:
        FileNotFoundError: If source_path path does not exist
        NotADirectoryError: If source_path exists but not a directory
    '''

    if not source_path.exists():
        raise FileNotFoundError(f'Path does not exist : {source_path}')
    if not source_path.is_dir():
        raise NotADirectoryError(f'Path exist but not a directory : {source_path}')
    
    files=[]

    if recursive:
        files=[item for item in source_path.rglob('*') if item.is_file()]
    else:
        files=[item for item in source_path.iterdir() if item.is_file()]
    
    return files