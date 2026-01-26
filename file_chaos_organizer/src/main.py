from pathlib import Path
from cli import parse_cli_args
from scanner import scan_directory
from config_loader import load_file_organization_rules
from mover import move_files
from undo_manager import undo_last_operation,save_operation_history

BASE_DIR=Path(__file__).resolve().parent.parent
RULES_FILE=BASE_DIR/'config'/'rules.ini'

def main():

    args=parse_cli_args()

    if args.undo:
        results=undo_last_operation()
        print(f'Undo completed : {len(results)} files restored')
        return

    source_dir=args.path
    recursive=args.recursive
    dry_run=args.dry_run

    files=scan_directory(source_dir,recursive)
    rules=load_file_organization_rules(RULES_FILE)

    results=move_files(
        files=files,
        base_dir=source_dir,
        rules=rules,
        dry_run=dry_run
    )

    if not dry_run:
        save_operation_history(results)
        print(f'Processed {len(results)} files')
    else:
        print('Dry run completed no files were moved')

if __name__=="__main__":
    main()