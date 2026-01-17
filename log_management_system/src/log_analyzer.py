from pathlib import Path
def analyze_logs(log_files:list):
    '''
    Analyze log files and count log levels.

    Args:
        log_files (List[Path]): List of log file paths
    Returns:
        dict[str,int]: count of log levels (INFO,ERROR,WARNING,DEBUG)
    Raises:
        ValueError: If log_files list is empty
        IOError: If any file cannot be read
    '''
    if not log_files:
        raise ValueError("No log files provided for analysis")
    
    log_levels_counts={
        'INFO':0,
        'ERROR':0,
        'WARNING':0,
        'DEBUG':0,
    }
    
    for log_file in log_files:
        try:
            with log_file.open(mode='r') as f:
                for line in f:
                    if line.startswith('INFO'):
                        log_levels_counts['INFO']+=1
                    elif line.startswith('ERROR'):
                        log_levels_counts['ERROR']+=1
                    elif line.startswith('WARNING'):
                        log_levels_counts['WARNING']+=1
                    elif line.startswith('DEBUG'):
                        log_levels_counts['DEBUG']+=1
        except OSError as e:
            raise IOError(f'Failed to read {log_file}') from e
    
    
    return log_levels_counts