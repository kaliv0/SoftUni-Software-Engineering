from typing import List
from task import Task
from more_itertools import first_true


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in [t.name for t in self.tasks]:
            return f"Could not find task with the name {task_name}"
        curr_task = first_true(self.tasks, None, lambda t: t.name == task_name)
        # task_index = self.tasks.index(curr_task)
        # self.tasks[task_index].completed = True
        curr_task.completed = True  # possible since it's a reference type but prone to errors
        return f"Completed task {task_name}"

    def clean_section(self):
        initial_length = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.completed is False]
        return f"Cleared {initial_length - len(self.tasks)} to-do-list."

    def view_section(self):
        return f"Section {self.name}:\n" + "\n".join([
            f"Name: {t.name} - Due Date: {t.due_date}" for t in self.tasks])


if __name__ == "__main__":
    task = Task("Make bed", "27/05/2020")
    print(task.change_name("Go to University"))
    print(task.change_due_date("28.05.2020"))
    task.add_comment("Don't forget laptop")
    print(task.edit_comment(0, "Don't forget laptop and notebook"))
    print(task.details())
    section = Section("Daily to-do-list")
    print(section.add_task(task))
    second_task = Task("Make bed", "27/05/2020")
    section.add_task(second_task)
    section.complete_task("Make bed")
    print(section.clean_section())
    print(section.view_section())
