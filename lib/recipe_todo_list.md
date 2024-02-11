## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

To create a list of tasks that are still to complete, a function to see the list, a function to add more tasks and a function to remove completed tasks


## 2. Design the Class Interface

basic draft

def __init__(self)
    self.task_list = []

def see_list():
    return f'this is your list of to do items: {self.task_list.items()}

def add_task(self, task):
    self.task_list.append(task)

def remove_completed_task(self, task):
    self.task_list.pop(task)

## 3. Create Examples as Tests

def test_todo_list()
    subject = ToDoList()
    subject.add_task('Meeting1')
    subject.add_task('Meeting2')
    subject.add_task('Meeting3')
    subject.add_task('Meeting4')
    subject.add_task('Meeting5')
    subject.add_task('Meeting6')
    assert subject.see_list() == ['Meeting1','Meeting2','Meeting3','Meeting4','Meeting5','Meeting6']
    subject.remove_completed_task('Meeting5)
    assert subject.see_list() == ['Meeting1','Meeting2','Meeting3','Meeting4','Meeting5','Meeting6']


## 4. Implement the Behaviour
