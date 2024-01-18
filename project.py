TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

# Example usage:
todo_list = TodoList()

while True:
    print('\nOptions:')
    print('1. Add Task')
    print('2. Remove Task')
    print('3. View Tasks')
    print('4. Quit')

    choice = input('Enter your choice (1/2/3/4): ')

    if choice == '1':
        task = input('Enter the task: ')
        todo_list.add_task(task)
    elif choice == '2':
        task = input('Enter the task to remove: ')
        todo_list.remove_task(task)
    elif choice == '3':
        todo_list.view_tasks()
    elif choice == '4':
        print('Exiting the to-do list application. Goodbye!')
        break
    else:
        print('Invalid choice. Please enter a valid option (1/2/3/4).')
