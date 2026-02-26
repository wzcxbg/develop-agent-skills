---
name: todo-list
version: "0.1.0"
description: Manage a simple todo list. Use this skill to add, list, complete, and remove tasks.
trigger: "manage todo list"
handler: scripts/todo_list.py
license: MIT
metadata:
  author: agent-skills-user
  dependencies: []
---

# Todo List Skill

This skill allows you to manage a simple todo list using a local JSON file.

## Usage

You can use the following commands:

- `add <task>`: Add a new task to the list.
- `list`: Show all tasks with their status.
- `complete <index>`: Mark a task as completed (using 1-based index).
- `remove <index>`: Remove a task from the list (using 1-based index).

## Example

To add a task:
```bash
python3 scripts/todo_list.py add "Buy milk"
```

To list tasks:
```bash
python3 scripts/todo_list.py list
```

To complete the first task:
```bash
python3 scripts/todo_list.py complete 1
```

To remove the second task:
```bash
python3 scripts/todo_list.py remove 2
```
