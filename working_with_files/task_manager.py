# This program is desgined to help manage tasks,
#  update and assign new tasks to memebers of the team.

# Import datetime library to help get the current date
#  at the time of assigning the new task.
import datetime

# Import os module to check if there are exisiting files
#  before generating them.
import os


def reg_user():
    '''Register a new user by taking in a username and a password as input 
    and storing them in a text file.'''
    new_username = input('Enter your new username here: \n').lower()

    # While loop to reiterate if user name is already taken.
    while new_username in usernames:
        print('Error, username already taken.')
        new_username = input('Enter your new username here: \n').lower()
    
    # Prompt the user for a new password and confirmation.
    new_password = input('Enter your password here: ')
    password_confirmation = input('Re-enter your password for confirmation: ')

    # Initalize attempts counter
    attempts = 3

    # Allow user to have a maximum of 3 attempts to confirm their password.
    while new_password != password_confirmation and attempts > 0:
        attempts -= 1
        print(f'Error: passwords do not match. {attempts} attempts remaining.')
        new_password = input('Enter your password here: ')
        password_confirmation = input('Re-enter your password for confirmation: ')
    
    if new_password == password_confirmation:
        print('New user created successfully.')
        with open('user.txt', 'a') as file:
            file.write(f'\n{new_username}, {new_password}')
    else:
        print('Maximum attempts reached, registration failed.')


# Function adds a task to the tasks text file.
def add_task():
    '''Add a task by taking task details as input and
    storing them in a text file.'''
    
    # Variables to get users input.
    # task_dis = Task discription
    task_assignment = input('Enter the name of the person whom the task is meant for: \n')
    title_task = input('Enter the title of the task \n')
    task_des = input('Enter the description of the task: \n')
    task_due_date = input('''Enter the due date for the task:
                          (e.g 25 Aug 2023)
                          (DD MON YYYY)\n''')
    task_due_date_formatted = datetime.datetime.strptime(task_due_date, '%d %b %Y').date()
    current_date = datetime.date.today()
    task_completion = 'No'

    # Open tasks text file and adds the new tasks to it.
    with open('tasks.txt', 'a') as file:
        file.write(f'\n{task_assignment}, {title_task}, {task_des}, {current_date.strftime("%d %b %Y")}, {task_due_date_formatted.strftime("%d %b %Y")}, {task_completion}')
    
    print('successfully added task.')


# Function displays tasks of all users.
def view_all_tasks():
    '''Display all tasks stored in a text file.'''

    # Open tasks text file and reads the information
    with open('tasks.txt', 'r') as file:
        # enumerate function to iterate through the file and give an index to
        # aspect of the task.
        for i, line in enumerate(file):
            task_content = line.strip().split(', ')
            prnt_task_info(i, task_content)


# Functiom to display the different information regarding the tasks.
def prnt_task_info(task_number, task_content):
    print(f'Task# {task_number + 1}')
    print(f'Task:             \t{task_content[1]}')
    print(f'Assigned to:      \t{task_content[0]}')
    print(f'Date Assigned:    \t{task_content[4]}')
    print(f'Due Date:         \t{task_content[3]}')
    print(f'Task Completed:   \t{task_content[5]}')
    print(f'Task Description: \t{task_content[2]}')
    
    print('')


# Function to update and save the edited task details to the tasks text file.
def update_task_file(task_lines):
    with open('tasks.txt', 'w') as file:
        for task_content in task_lines:
            task_line = ', '.join(task_content)
            file.write(f'{task_line}\n')


# Function created to display all the tasks of a specific user.
def view_mine():
    task_lines = []  # Store tasks lines for a specific user.
    
    with open('tasks.txt', 'r') as file:
        for line in file:
            task_content = line.strip().split(', ')
            if task_content[0] == user_name:
                task_lines.append(task_content)
        
    if not task_lines:
        print('There are no tasks found for this user.\n')
        return
    
    for i, task_content in enumerate(task_lines):
        prnt_task_info(i, task_content)

    while True:
        edit_task = int(input('Enter the task number to edit (or enter -1 to exit): '))

        # If user selects -1, end program and return to main menu.
        if edit_task == -1:
            break
        # If user input is greater than -1 and 
        # not greater than the amount of users
        elif edit_task >= 1 and edit_task <= len(task_lines):
            task_index = edit_task - 1
            task_assigned_to = task_lines[task_index][0]
            task_completed = task_lines[task_index][5]

            # Check if the task is completed or not.
            if task_completed == 'No':
                print(f'Task #{edit_task}:')
                print(f'Task Title:       \t{task_lines[task_index][1]}')
                print(f'Assigned to:      \t{task_assigned_to}')
                print(f'Date Assigned:    \t{task_lines[task_index][3]}')
                print(f'Due Date:         \t{task_lines[task_index][4]}')
                print(f'Task Completed:   \t{task_completed}')
                print(f'Task Description: \t{task_lines[task_index][2]}: ')
                print('')

                edit_option = input('Choose an option:\n1. Mark task as complete\n2. Edit task\nEnter option (1/2): ')

                # Check the input from user, and
                # carry out changes as per user unput
                if edit_option == '1':
                    task_lines[task_index][5] = 'Yes'
                    print('Task marked as complete.')
                elif edit_option == '2':
                    edited_task = edit_task_details(task_lines[task_index])
                    task_lines[task_index] = edited_task
            else:
                print('Task is already marked as complete and cannot be edited')
        else:
            print('Invalid task number.')
    
    # Update the task details in the task text file.
    update_task_file(task_lines)
    

# Function to edit the name, and due date of a task.
def edit_task_details(task_content):
    print('Edit Task Details:')

    # Prompt user for new assigned person and date.
    new_assignee = input('Enter the new assigned person (leave empty to keep unchanged): ')
    new_due_date = input('Enter the new due date(YYYY-MM-DD, leave empty to keep unchanged.): ')

    if new_assignee:
        task_content[0] = new_assignee
    if new_due_date:
        task_content[4] = new_due_date

    print('Task details updated.')
    return task_content


# Function to generate a task overview report and user overview report.
def generate_reports():
    # variables to calculate tasks overview statistics.
    total_tasks = 0
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0

    # Initalize the datetime object to get the current date.
    current_date = datetime.date.today()

    with open('tasks.txt', 'r') as file:
        for line in file:
            total_tasks += 1
            task_content = line.strip().split(', ')
            if task_content[5] == 'Yes':
                completed_tasks += 1
            else:
                incomplete_tasks += 1
                due_date = datetime.datetime.strptime(task_content[4], '%d %b %Y').date()
                if due_date < current_date:
                    overdue_tasks += 1

    # Checks if there are no tasks first to avoid ZeroByDivision Error.
    if total_tasks == 0:
        incomplete_tasks = 0
        overdue_tasks = 0
    else:
        incomplete_percentage = ((incomplete_tasks / total_tasks) * 100)
        overdue_percentage = ((overdue_tasks / total_tasks) * 100)

    # Write tasks overview report to text file.
    with open('task_overview.txt', 'w') as file:
        file.write(f'Task Overview Report: \n')
        file.write(f'Total number of tasks:                  {total_tasks}\n')
        file.write(f'Total number of completed tasks:        {completed_tasks}\n')
        file.write(f'Total number of incompleted tasks:      {incomplete_tasks}\n')
        file.write(f'Total number of tasks that are overdue: {overdue_tasks}\n')
        file.write(f'Percentage of incomplete tasks:         {round(incomplete_percentage,2)}%\n')
        file.write(f'Percentage of overdue tasks:            {round(overdue_percentage,2)}%')
    
    # Get the total number of users.
    total_users = len(usernames)

    with open('user.txt', 'r') as file:
        user_task_counts = {username: 0 for username in usernames}

        for line in file:
            content = line.strip().split(', ')
            username = content[0]
            user_task_counts[username] += 1
    
    # Write the stattistics to user overview text file.
    with open('user_overview.txt', 'w') as file:
        file.write('User Overview Report: \n')
        file.write(f'Total users: {total_users}\n')

        for username in usernames:
            total_user_tasks = user_task_counts[username]
            # Check if the total number of user tasks is not zero to
            # prevent Zero By Division Error.
            if total_user_tasks == 0:
                user_task_percentage = 0
                user_completed_percentage = 0
                user_incomplete_percentage = 0
                user_overdue_percentage = 0
            else:
                user_task_percentage = (total_user_tasks / total_tasks) * 100
                user_completed_percentage = (completed_tasks / total_user_tasks) * 100
                user_incomplete_percentage = ((total_user_tasks - completed_tasks) / total_user_tasks) * 100
                user_overdue_percentage = (overdue_tasks / total_user_tasks) * 100
            
        file.write(f'\nUser: {username}\n')
        file.write(f'Total number of tasks assigned:           \t\t{total_user_tasks}\n')
        file.write(f'Percentage of total tasks:                    {round(user_task_percentage, 2)}%\n')
        file.write(f'Percentage of tasks completed:                {round(user_completed_percentage, 2)}%\n')
        file.write(f'Percentage of tasks incompleted:              {round(user_incomplete_percentage, 2)}%\n')
        file.write(f'Percentage of overdue tasks:                  {round(user_overdue_percentage, 2)}%\n')


# Function checks if there are existing reports, if not
# generates them, then displays the information.
def view_statistics():
    # Check if the report exists, if not, generate them.
    if not (os.path.isfile('task_overview.txt') and os.path.isfile('user_overview.txt')):
        generate_reports()
    
    # Read and Display the task overview report
    with open('task_overview.txt', 'r') as file:
        task_overview = file.read()
        print(task_overview)


# Variables to store the list of names and passwords.
usernames = []
passwords = []


with open('user.txt', 'r') as file:
    # Create a for loop to help read the file.
    # Then strip the newlines (\n) from the text file
    # and append the usernames and passwords to a list.
    for lines in file:
        content = lines.strip()
        content = content.split(', ')
        usernames.append(content[0])
        passwords.append(content[1])

# Initialize a variable to track successful login.
login_successful = False

# Prompts the user to enter username and password.
while not login_successful:
    user_name = input('Enter your username: \n').lower()
    pass_word = input('Enter your password: \n')
    
    # If user_name is in usernames list and pass_word
    # in password list, print a relevant message.
    for i in range(len(usernames)):
        if usernames[i] == user_name and passwords[i] == pass_word:
            print('Login Successful')
            login_successful = True
            break

    # If not print an error message.    
    if not login_successful:
        print('Invalid username or password. Please try again.')

print('')

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user  (admin only)
a - add task
gr - generate reports
va - view all tasks
vm - view my tasks
vs - view statistics (admin only)
e - exit
: ''').lower()

    if menu == 'r':
        if user_name == 'admin':
            reg_user()
            print('')
        else:
            print('Only admin may register new users.')
            print('')
                             
    elif menu == 'a':
        add_task()
        print('')
    
    elif menu == 'gr':
        generate_reports()
        print('Reports generated successfully.')
        print('')

    elif menu == 'va':
        view_all_tasks()
        print('')

    elif menu == 'vm':
        view_mine()
        print('')
        
    elif menu == 'vs':
        # Allows only admin access.
        if user_name == 'admin':
            view_statistics()
            print('')
        else:
            print('Only admin may access statistics.')
            print('')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")
