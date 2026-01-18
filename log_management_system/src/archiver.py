from pathlib import Path
from datetime import datetime

def archive_logs(log_files:list,archive_dir:Path):
    '''
    Archives all the processed log files by moving processed log files into archive_dir , safely Handles name collisions

    Args:
        log_files (list[Path]): List of log file paths
        archive_dir (Path): directory path to which all the log files will be archived 
    Returns:
        List[Path]: List of all archived files paths
    Raises:
        ValueError: If log_files is empty
        NotADirectoryError: If archive_dir exist but not as a directory 
        FileNotFoundError: If log file does not exist
        IOError: If failed to move file
    '''

    if not log_files:
        raise ValueError("Log files are empty")
    if archive_dir.exists() and not archive_dir.is_dir():
        raise NotADirectoryError(f'{archive_dir} does not exist as a directory')
    
    archive_dir.mkdir(parents=True,exist_ok=True)

    archived_file_paths=[]

    for log_file in log_files:
        if not log_file.exists():
            raise FileNotFoundError(f'Log file does not exist {log_file}')
        
        destination=archive_dir/log_file.name

        if destination.exists():
            timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            destination=archive_dir/f'{log_file.stem}_{timestamp}{log_file.suffix}'
        try:
            log_file.rename(destination)
            archived_file_paths.append(destination)
        except OSError as e:
            raise IOError(f'Failed to move file {log_file.stem}') from e
            
    return archived_file_paths
    