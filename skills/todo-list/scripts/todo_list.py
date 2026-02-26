#!/usr/bin/env python3
import sys
import json
import os
import argparse

TODO_FILE = "todo.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def add_todo(task):
    todos = load_todos()
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    print(f"Added task: {task}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
        return
    for i, todo in enumerate(todos):
        status = "[x]" if todo["completed"] else "[ ]"
        print(f"{i + 1}. {status} {todo['task']}")

def complete_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]["completed"] = True
        save_todos(todos)
        print(f"Completed task: {todos[index]['task']}")
    else:
        print("Invalid task index.")

def remove_todo(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"Removed task: {removed['task']}")
    else:
        print("Invalid task index.")

def main():
    parser = argparse.ArgumentParser(description="Simple Todo List Manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="The task description")

    list_parser = subparsers.add_parser("list", help="List all tasks")

    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("index", type=int, help="Task index (1-based)")

    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("index", type=int, help="Task index (1-based)")

    args = parser.parse_args()

    if args.command == "add":
        add_todo(args.task)
    elif args.command == "list":
        list_todos()
    elif args.command == "complete":
        complete_todo(args.index - 1)
    elif args.command == "remove":
        remove_todo(args.index - 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
