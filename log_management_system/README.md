# Project 1: Log Management & Analytics System

This project simulates a real-world log processing system used in production environments.

A **production-style log management and automation system** built using Python.  
This project demonstrates how real-world backend and automation tools are structured, configured, and executed in professional environments.

The system scans log files, analyzes log levels, generates reports, archives processed logs, and sends notifications about success or failure — all with clean modular design and configuration support.

---

## Constraints
- No OOP
- Standard library only
- Modular, production-style design

---

## 📌 Features

- Scan directories for `.log` files
- Analyze log levels (`INFO`, `ERROR`, `WARNING`, `DEBUG`)
- Generate timestamped analysis reports
- Archive processed log files safely (collision-aware)
- Persist success/failure notifications
- Configuration-driven (no hardcoded paths)
- Fail-safe orchestration with proper error propagation
- Clean, testable, and maintainable structure

---

## 🏗 Project Structure

```
log_management_system/
├── config/
│   └── config.ini
├── logs/
├── reports/
├── archives/
├── notifications/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config_loader.py
│   ├── log_scanner.py
│   ├── log_analyzer.py
│   ├── report_generator.py
│   ├── archiver.py
│   └── notifier.py
└── README.md
```

---

## ⚙️ Configuration

All paths are configured via an external configuration file.

### `config/config.ini`
```ini
[paths]
log_dir = logs
report_dir = reports
archive_dir = archives
notify_dir = notifications
```

This allows the same codebase to run across different environments without modification.

---

## 🚀 How It Works

1. **Scan Logs** – Detects `.log` files from the configured log directory  
2. **Analyze Logs** – Counts log levels across all files  
3. **Generate Report** – Saves a summary report with timestamps  
4. **Archive Logs** – Moves processed logs into an archive directory  
5. **Notify Status** – Writes success or failure notifications  

If any stage fails, the system:
- Sends a failure notification
- Stops execution
- Re-raises the exception (no silent failures)

---

## ▶️ Running the Project

From the project root:

```bash
python src/main.py
```

Ensure:
- `config/config.ini` exists
- Required directories are present (they will be created if missing)

---

## 🧠 Design Principles Used

- **Single Responsibility Principle**
- **Separation of Configuration and Code**
- **Fail Fast, Fail Loud**
- **No Side Effects on Import**
- **Production-Grade Error Handling**
- **Clear Orchestration Layer**

---

## 📂 Notifications

Each run generates a notification file in the `notifications/` directory containing:
- Event name
- Status (`SUCCESS` / `FAILED`)
- Timestamp
- Contextual metadata

This mimics real-world operational alerting systems.

---

## 🧪 Testing Strategy (Current)

- Deterministic functions
- No logic executed on import
- Clear boundaries for future unit tests

---

## 🛣 Future Enhancements

- CLI arguments (`argparse`)
- Dry-run mode
- Structured logging (`logging` module)
- Exit codes for automation tools
- Unit tests
- OOP-based refactor

---

## 👨‍💻 Author

Built as part of an advanced Python engineering learning journey, focused on **real-world practices**, **production readiness**, and **professional coding standards**.

[Abdul Aziz Shaik](https://github.com/ShaikAbdulAzizGit)

---

## 📄 License

This project is intended for learning and portfolio purposes.
