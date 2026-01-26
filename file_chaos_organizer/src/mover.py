from pathlib import Path
from datetime import datetime
from categorizer import categorize_file

def move_files(files:list[Path],base_dir:Path,rules:dict[str,list[str]],dry_run:bool=False)->list[dict]:
    '''
    Move files into categorized folders
    Args:
        files:list[Path]: Files to organize
        base_dir(Path): Base directory where categorization will be performed
        rules(dict[str,list[str]]): categorization rules
        dry_run: If true ,No files are moved
    Returns:
        results(list[dict]): Movement result metadate for each file
    '''

    results=[]

    for file_path in files:
        category=categorize_file(file_path,rules)
        target_dir=base_dir/category
        target_dir.mkdir(parents=True,exist_ok=True)

        destination=target_dir / file_path.name

        # Handle File name collisions
        if destination.exists():
            time_stamp=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            destination=target_dir/f'{file_path.stem}_{time_stamp}{file_path.suffix}'
        
        action='preview'
        if not dry_run:
            try:
                file_path.rename(destination)
                action='moved'
            except Exception as e:
                results.append({
                        'source':str(file_path),
                        'destination':None,
                        'status':'failed',
                        'error':str(e)
                    })
                continue    
        results.append(
            {
                'source':str(file_path),
                'destination':str(destination),
                'status':action
            }
        )

    return results