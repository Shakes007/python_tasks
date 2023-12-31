# This repository contains programs developed in python.

## Calculator Application:
- This is a basic calculation app that creates different functions for each operation.
- It also imports the numpy library to make the calculations easier.
- Lastly, there is a menu for the user to select from.
- Upon selection and completetion of the operation, the calculation will then be saved to a file called equations.txt
- There is user-frinedly documentation explaining the different functions in docs/_build/html/calc_app.html

## Financial Calculator:
- This calculator is special due to its ability to either calculate bond repayments or return on investments.
- it also imports the math library to make use of interest formulae and to make calculations easier.
- This program makes use of if and else statements and offers the user a menu to select their course of action.
- Baased on what the user selects, the program will excecute accordingly.

## Recursion
- In this folder there are two programs called largest_number.py and sum_recursion.py

### _largest_number.py_
- This program uses a user-defined function called largest_number() and takes in a list.
- Within the function it searches for the largest number in the list and does this recursively.
- Documentation can be found in docs/_build/html/largest_number.html.

### _sum_recursion.py_
- This program takes input from the user. The user has to enter enough numbers to form a list.
- The program will then execute and calculate the sum of the list.
- There is one user-defined function called add_up_to() and takes in two parameters:
  _list_ and _index_.
- The program will then calculate the sum of the given list recursively.
- Documentation for this can be found in docs/_build/html/sum_recursion.html

## Working with files:
- This is a task manager program that is designed to help manage tasks efficently, update and assign
new tasks to members.
- This program imports the datetime and os libraries.
- It has several user-defined functions such as
  * reg_user()
  * add_task()
  * view_all_tasks()
  * update_task_file()
    and more.
- All tasks and users are saved to a tasks.txt and users.txt
- The program has a login section which either admin or members of the team may login.
- Admin has some functions which other memebers may not use.
- Finally, a menu is generated upon successful login and gives the user a range of options to select from.
- Documentation can be found for the entire program in docs/_build/html/task_manager.html

**All documentation was generated using Sphinx**
