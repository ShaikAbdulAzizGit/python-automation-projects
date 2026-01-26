from pathlib import Path
from configparser import ConfigParser

def load_file_organization_rules(config_file_path:Path)->dict:
    '''
    loads rules for organizing files from rules.ini

    Args:
        config_file_path(Path): Path to rules.ini file
    Returns:
        rules(dict[str,list]): Contains suitable extensions for a particular file section ex(IMAGES:[.jpg,.png,.gif])
    Raises:
        FileNotFoundError: If config_file_path does not exist
        ValueError: If config_file_path file is empty
        ValueError: If config_file_path does not contain any sections
        IOError: If Failed to read config_file_path
    
    '''
    if not config_file_path.exists():
        raise FileNotFoundError(f'Path does not exist : {config_file_path}')
    if  config_file_path.stat().st_size==0:
        raise ValueError(f'{config_file_path} is empty')
    
    parser=ConfigParser()

    try:
        parser.read(config_file_path)
    except OSError as e:
        raise IOError(f'Failed to read {config_file_path.name}') from e
    
    if not parser.sections():
        raise ValueError('No categories defined in rules.ini file')
    
    rules={}

    for section in parser.sections():
        extensions=parser[section].get('extensions','')
        rules[section]=[ex.lower().strip() for ex in extensions.split(',') if ex]

    return rules