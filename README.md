# Agent Skills Repository

This repository contains a collection of skills for AI agents, following the [Agent Skills](https://agentskills.io) standard.

## Structure

- `skills/`: Contains the source code for each skill.
- `tests/`: Contains unit tests for the skills.
- `docs/`: Documentation.

## Available Skills

### Todo List Skill

A simple skill to manage a todo list.

**Features:**
- Add tasks
- List tasks
- Complete tasks
- Remove tasks

**Installation:**

You can install this skill using the `agent-skills-cli`:

```bash
# Install from local directory
skills add ./skills/todo-list

# Or if hosted on GitHub
skills add <owner>/<repo> --skill todo-list
```

**Usage:**

Once installed, the agent can use the skill by matching the description or explicit invocation.

Example prompts:
- "Add 'Buy milk' to my todo list"
- "Show my todos"
- "Mark the first task as done"

**Manual Execution:**

You can also run the skill manually:

```bash
python3 skills/todo-list/scripts/todo_list.py --help
```

## Development

To create a new skill:

```bash
skills init <skill-name>
```

To run tests:

```bash
python3 -m unittest discover tests
```
