import unittest
import sys
import os
import json
import shutil
import tempfile
from io import StringIO

# Add scripts directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../skills/todo-list/scripts'))
import todo_list

class TestTodoList(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)
        
        # Capture stdout
        self.held_stdout = sys.stdout
        self.stdout = StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.held_stdout
        
        # Restore cwd and remove temp dir
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_add_todo(self):
        todo_list.add_todo("Buy milk")
        self.assertTrue(os.path.exists("todo.json"))
        with open("todo.json", 'r') as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['task'], "Buy milk")
        self.assertFalse(data[0]['completed'])

    def test_list_todos_empty(self):
        todo_list.list_todos()
        output = self.stdout.getvalue()
        self.assertIn("No tasks found.", output)

    def test_list_todos_populated(self):
        todo_list.add_todo("Task 1")
        todo_list.add_todo("Task 2")
        self.stdout.seek(0)
        self.stdout.truncate(0)
        
        todo_list.list_todos()
        output = self.stdout.getvalue()
        self.assertIn("1. [ ] Task 1", output)
        self.assertIn("2. [ ] Task 2", output)

    def test_complete_todo(self):
        todo_list.add_todo("Task 1")
        todo_list.complete_todo(0)
        
        with open("todo.json", 'r') as f:
            data = json.load(f)
        self.assertTrue(data[0]['completed'])

    def test_remove_todo(self):
        todo_list.add_todo("Task 1")
        todo_list.add_todo("Task 2")
        todo_list.remove_todo(0)
        
        with open("todo.json", 'r') as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['task'], "Task 2")

if __name__ == '__main__':
    unittest.main()
