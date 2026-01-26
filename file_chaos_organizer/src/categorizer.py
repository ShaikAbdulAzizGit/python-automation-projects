from pathlib import Path

def categorize_file(file_path:Path,rules:dict[str,list[str]])->str:
    '''
    Categorize file based on it's extension
    Args:
        file_path(Path): file to categorize
        rules(dict[str,list[str]]): Rules for file categorization
    Returns:
        category(str): Category name of the file
    '''

    extension=file_path.suffix.lower()

    for category,extensions in rules.items():
        if extension in extensions:
            return category
    
    return 'Others'