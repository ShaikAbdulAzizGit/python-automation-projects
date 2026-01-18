from log_scanner import scan_log_files
from log_analyzer import analyze_logs
from report_generator import generate_report
from archiver import archive_logs
from notifier import notify
from pathlib import Path


BASE_DIR=Path(__file__).resolve().parent.parent

LOG_DIR=Path(BASE_DIR,'logs')
REPORT_DIR=Path(BASE_DIR,'reports')
ARCHIVE_DIR=Path(BASE_DIR,'archives')
NOTIFY_DIR=Path(BASE_DIR,'notifications')

def main():
    try:
        # Stage 1: Scan logs
        log_file_paths=scan_log_files(LOG_DIR)
        # Stage 2: Analyze logs
        log_level_counts=analyze_logs(log_file_paths)
        # Stage 3: Generate report
        report_file_path=generate_report(log_level_counts,REPORT_DIR)
        # Stage 4: Archive logs
        archived_file_paths=archive_logs(log_file_paths,ARCHIVE_DIR)
        # Stage 5: Notify Success
        meta_data={
            'log_files_processed':len(log_file_paths),
            'archived_files':len(archived_file_paths),
            'report_path':str(report_file_path)
        }
        notify(
            event='log_processing',
            status='SUCCESS',
            meta_data=meta_data,
            notify_dir=NOTIFY_DIR
        )
    except Exception as e:
        meta_data={
            'error':str(e),
            'stage':'main_orchestration'
        }
        notify(
            event='log_processing',
            status='FAILED',
            meta_data=meta_data,
            notify_dir=NOTIFY_DIR
        )
        raise

if __name__=='__main__':
    main()