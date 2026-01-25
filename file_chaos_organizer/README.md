# File Chaos Organizer

File Chaos Organizer is a **safe, configurable, and cross-platform Python automation tool**
that helps users organize messy folders (such as Downloads or Desktop) into clean,
well-structured directories.

The tool is designed with **real-world safety guarantees** such as dry-run previews,
duplicate protection, undo support, and detailed logging. It is built without using
object-oriented programming, focusing instead on clean modular functions and
production-grade scripting practices.

---

## 🚨 The Problem

Most users download files daily and never clean them.
Over time, folders become cluttered, files become hard to find,
storage gets wasted due to duplicates, and important documents
risk being overwritten or lost.

Manual cleanup is time-consuming, repetitive, and error-prone.

---

## ✅ What This Tool Does

- Automatically categorizes files by type (Images, Documents, Videos, Archives, etc.)
- Detects and safely handles duplicate files
- Organizes files by date (Year / Month structure)
- Supports custom user-defined categorization rules
- Provides a **dry-run (safe preview) mode**
- Logs all actions for traceability and debugging
- Allows undoing the last organization operation
- Works on Windows, Linux, and macOS

---

## 🛡 Safety-First Design

This project is built with **data safety as a top priority**:

- No files are overwritten
- Dry-run mode previews all actions before execution
- Undo feature allows rollback of the last operation
- Permission and access errors are handled gracefully
- All actions are logged for auditability

These guarantees make the tool safe for both technical and non-technical users.

---

## 🧰 Planned CLI Usage

```bash
python src/main.py --path ~/Downloads --recursive
python src/main.py --path ~/Desktop --dry-run
python src/main.py --undo
```

---

## 📁 Project Structure (High-Level)

```
file_chaos_organizer/
├── config/        # User-defined categorization rules
├── logs/          # Action and error logs
├── state/         # Metadata for undo operations
├── src/           # Application source code
└── README.md
```

---

## 🧠 Design Philosophy

This project follows real-world engineering principles:

- Clear separation of concerns
- Predictable and reversible automation
- Configuration-driven behavior (no hardcoding)
- Fail-safe execution with meaningful logs
- Maintainability over cleverness

The goal is not just to organize files, but to build a tool
that users can trust with their data.

---

## 📌 Project Status

This project is under active development.
Features are implemented incrementally with strict version control
and professional commit discipline.
