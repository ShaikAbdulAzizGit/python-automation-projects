from pathlib import Path
from datetime import datetime
def generate_report(log_level_counts:dict,report_directory_path:Path):
    '''
    Generate log analysis report and save it into the disk 

    Args:
        log_level_counts (dict[str,int]): Log level count (INFO,ERROR,WARNING,DEBUG)
        report_directory_path (Path): Path for the directory to save report.txt files
    Returns:
        Path to the generated report file
    Raises:
        ValueError: If the log_level_counts data is empty
        NotADirectoryError: If report directory path does not exist as a directory
        IOError: If failed to write into report file 
    '''
    if not log_level_counts:
        raise ValueError('Analysis Data is Empty')
    if report_directory_path.exists() and not report_directory_path.is_dir():
        raise NotADirectoryError(f'Path does not exist as directory : {report_directory_path.name}')
    
    report_directory_path.mkdir(parents=True,exist_ok=True)
    
    info=log_level_counts.get('INFO',0)
    error=log_level_counts.get('ERROR',0)
    warning=log_level_counts.get('WARNING',0)
    debug=log_level_counts.get('DEBUG',0)
    report_content=f'''
Date: {datetime.now().date()}
---------------------------------
INFO: {info}
ERROR: {error}
WARNING: {warning}
DEBUG: {debug}
---------------------------------
Total log entries: {info+error+warning+debug}
'''
    report_file_name=f"log_report_{datetime.now().strftime('%Y_%m_%d')}.txt"
    report_path=report_directory_path/report_file_name

    try:
        report_path.write_text(report_content)   
    except OSError as e:
        raise IOError(f'Failed to write into {report_path.name}') from e
        
    return report_path
