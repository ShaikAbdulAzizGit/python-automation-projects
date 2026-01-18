from pathlib import Path
from datetime import datetime

def notify(event:str,status:str,meta_data:dict,notify_dir:Path):
    '''
    persist a notification about system events 

    Args:
        event (str): Name of the event (e.g., "log_processing)
        status (str): SUCCESS or FAIL
        meta_data (dict): Contextual Information
        notify_dir (Path): Path of the directory to persist notification.txt files

    Returns:
        notification_file_path (Path):Path to the generated notification.txt file 
    
    Raises:
        ValueError: If any of the input data is empty
        NotADirectoryError: notify_dir path exist but not a folder
        IOError: If Failed to write into notification.txt file
    '''

    if not event or not status:
        raise ValueError('Event and Status are required')
    
    if notify_dir.exists() and not notify_dir.is_dir():
        raise NotADirectoryError(f'Path exist but not a directory : {notify_dir}')
    
    notify_dir.mkdir(parents=True,exist_ok=True)

    meta_data_lines=[]

    for key,value in meta_data.items():
        meta_data_lines.append(f'-> {key}:{value}')

    meta_data_block='\n'.join(meta_data_lines) if meta_data_lines else '--None'
    
    time_stamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    notification_content=f'''
Event: {event}
Status: {status}
Timestamp: {time_stamp}
Details:
{meta_data_block}
    '''
    notification_file_time_stamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    notification_file_name=f'{event}_{status}_{notification_file_time_stamp}.txt'

    notification_file_path=notify_dir/notification_file_name
    
    try:
        notification_file_path.write_text(notification_content)
    except OSError as e:
        raise IOError(f'Failed to write into {notification_file_path}')

    return notification_file_path
    