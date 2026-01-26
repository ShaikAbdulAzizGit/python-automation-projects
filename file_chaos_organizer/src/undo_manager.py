from pathlib import Path
import json

HISTORY_DIR=Path(__file__).resolve().parent.parent/'state'
LAST_OPERATION_FILE=HISTORY_DIR/'last_operation.json'

def save_operation_history(results:list[dict]):
    '''
    save file move history in json file for undo functionality
    Args:
        results:list[dict]: results of successfully moved files
    Returns: 
        None
        
    '''
    HISTORY_DIR.mkdir(exist_ok=True)

    moved_files=[
        {
            'source':r['source'],
            'destination':r['destination']

         }
         for r in results if r.get('status')=='moved'
    ]

    if not moved_files:
        return
    
    with LAST_OPERATION_FILE.open(mode='w',encoding='utf-8') as f:
        json.dump(moved_files,f,indent=2)


def load_last_operation():
    '''
    Loads history of last operatoin from json file
    '''
    if not LAST_OPERATION_FILE.exists():
        raise FileNotFoundError('No operation history found to undo changes')
    with LAST_OPERATION_FILE.open(mode='r',encoding='utf-8') as f:
        return json.load(f)


def undo_last_operation():
    '''
    Restore files to the previous state
    Returns:
        results(list[dict]): Results for restored files
    '''

    operations=load_last_operation()

    results=[]
    for entry in operations:
        source=Path(entry['source'])
        destination=Path(entry['destination'])

        if not destination.exists():
            results.append({
                'source':str(destination),
                'destination':str(source),
                'status':'failed',
                'error':'destination file not found'
            })
            continue

        try:
            source.parent.mkdir(parents=True,exist_ok=True)
            destination.rename(source)
            results.append({
                'source':str(destination),
                'destination':str(source),
                'status':'restored'
            })
        except Exception as e:
            results.append({
                'source':str(destination),
                'destination':str(source),
                'status':'failed',
                'error':str(e)
            })

    return results
