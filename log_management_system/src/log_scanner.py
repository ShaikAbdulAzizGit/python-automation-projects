from pathlib import Path

def scan_log_files(directory_path:Path):
    '''
    Scan the directory and returns all .log files in a list

    Args:
        log_dir (Path): Directory containing log files

    Returns:
        List(Path): List of .log file paths

    Raises:
        FileNotFoundError: If the file does not exist
        NotADirectoryError: If the path is not a direcotory
        ValueError: If No .log files are found in directory 
           
    '''
    if not directory_path.exists():
        raise FileNotFoundError(f'{directory_path.name} does not exist')
    
    if not directory_path.is_dir():
        raise NotADirectoryError(f'{directory_path.name} is not a directory')
    
    log_files=list(directory_path.glob('*.log'))

    if not log_files:
        raise ValueError(f'No .log files found in directory : {directory_path.name} ')
    return log_files


