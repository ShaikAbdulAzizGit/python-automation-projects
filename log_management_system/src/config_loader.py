from configparser import ConfigParser
from pathlib import Path

def load_config(config_file_path:Path) -> dict:
    '''
    Loads application configuration from config.ini file 

    Args:
        config_file_path (Path): Path to the config.ini file
    Returns:
        config_data (Dict): Structured data of config.ini file of [paths] section
    Raises:
        FileNotFoundError:If config_file_path does not exist
        ValueError:If config.ini file is empty
        ValueError:If paths section is missing in config.ini file
        KeyError:If Any of ['log_dir','report_dir','archive_dir','notify_dir'] keys missed in config.ini file
        IOError:IF failed to read config.ini file
    '''

    if not config_file_path.exists():
        raise FileNotFoundError(f'Path does not exits {config_file_path}')
    if config_file_path.stat().st_size <=0:
        raise ValueError(f'config file is empty {config_file_path}')

    

    config_parser=ConfigParser()
    try:
        config_parser.read(config_file_path)
    except OSError as e:
        raise IOError(f'Failed to read {config_file_path.name}') from e

    if 'paths' not in config_parser:
        raise ValueError(f'Missing [paths] section in config file {config_file_path}')
    
    required_keys=['log_dir','report_dir','archive_dir','notify_dir']

    missing_keys=[key for key in required_keys if key not in config_parser['paths']]

    if missing_keys:
        raise KeyError(f'Missing config keys : {missing_keys}')
    
    
    config_data={key:value for key,value in config_parser['paths'].items()}

    return config_data



    