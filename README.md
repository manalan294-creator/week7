# plp-python-week7

This repository contains the files for the Shopping List Manager assignment.

- `list_warmup.py`: demonstrates list indexing, appending, removing, and length checks.
- `shopping_list.py`: creates a simple interactive shopping list manager with add, remove, show, and done actions.
- `list_report.py`: prints a numbered list, counts long item names, and finds the longest item name.

It is safer to check whether an item is in a list before calling `.remove()` because this prevents runtime errors and avoids accidentally deleting something that is not there. It also makes the program more user-friendly and prevents crashes during normal use.
