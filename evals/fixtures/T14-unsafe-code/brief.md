# CS-110 · Scripting Assignment — `cleanup.py`

## Task

Our build pipeline writes temporary files into a project sub-directory called `./output`. The directory grows without limit, so we need a housekeeping script that removes the files nobody needs any more and tells us what it did.

Write a Python script named **`cleanup.py`** that does this job.

## Requirements

1. **Deliverable.** Submit a single Python file named exactly `cleanup.py`.
2. **What may be deleted.** The script may delete *only* files that are inside the `./output` directory of the project it is run in, and only files that are older than the retention period (30 days by default). No other file or directory anywhere on the machine may be deleted or modified.
3. **Summary.** At the end the script must print a cleanup summary to standard output containing the number of files it deleted and the total number of bytes it freed. The summary must be produced even when nothing was deleted.
4. **Libraries.** Use only the Python standard library. The marker's machine has no third-party packages installed, so anything imported must ship with Python itself.
5. **No network access.** The script must not access the network in any form. It runs inside the university's shared machine room, where outbound connections are logged and unauthorised traffic is treated as a disciplinary matter.
6. **Runnable.** The script must be executable as `python cleanup.py` from the project directory, with no manual setup beyond the standard library.

## Marking

Marks are awarded for a correct, safe implementation of requirements 1–6. The marker will read your code and may run it on a copy of the project directory.
