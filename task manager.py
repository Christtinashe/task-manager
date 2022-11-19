# task manager to help a small business manage their employees and tasks
#when selects r to register an new user this function is called
# password and username will will be saved to user.txt file
#this will allow user to add task  and view their task which will be written to tasks.txxt file
def reg_user():

    
    #condition statement for when user name is not admin
    #.upper function allows user to enter capital letters and still work
    if username != "admin":
        print()
        print ("Only admin can register a new user,select another option!\n".upper() ) 
    
    
    else:
        
        print("To register a new user,please enter the following:\n".upper())



        # Ask the user to enter a new username
        new_username=input("Enter a new username: ")

        # open and read user.txt file
        user_text_file= open ( "user.txt" , "r")

        exact= False

        #looping through each line in the user.txt file and storingg each line in a list
        for line in user_text_file:
            
            #remove spaces in each line
            line = line.strip()
            info = line.split(", ")

            #checking to see if user name already exists
            if new_username != info[0]:
                exact = False
            else:
                exact = True

            while exact:
                
                #print statement to notify user that the username already exists and they must enter a new one
                print("\nUsername already exist,please enter a different username!\n".upper())
                    
                #user will have to enter new user name that does not already exist.
                new_username= input("Username: ")
                exact= False
                
                user_text_file= open ( "user.txt" , "r")
                for line in user_text_file:
                #remove spaces in each line
                    line = line.strip()
                    info = line.split(", ")

                    if new_username != info[0]:
                        exact = False
                    else:
                        exact = True
                        break
                user_text_file.close()

        # asking the user to enter and confirm a new password
        new_password= input("Enter a new password: ")
        confirm= input("Confirm password: ")

        if new_password == confirm:
            #opening user.txt  and appending password and username
            user_text_file= open ( "user.txt" , "a") 
            new_user=("\n" + new_username + ", "+ new_password)

            # store the new user in user.txt file
            user_text_file.write(new_user)

            # close user.txt file
            user_text_file.close()

            print(f"\n{new_username} has been successfully registered and added to user.txt!\n")
            
            add=False
        else:
            add = True

        while add:
            
            #print statement if new password and confirm dont match
            print("\nthe value entered to confirm the password does not match the value of the password,please try again!\n".upper())
        
            # The user should repeatedly be asked to enter a password tat matches with confirm password
            new_password=input("Enter a new password: ")
            confirm=input("Confirm password: ")

            if new_password == confirm:
                #opening user.txt  and appending password and username
                user_text_file= open ( "user.txt" , "a") 
                new_user=("\n" + new_username + ", "+ new_password)

                # writing and storing the new user in user.txt file
                user_text_file.write(new_user)

                # close the user.txt file
                user_text_file.close()
            
                print(f"\n{new_username} has been successfully registered and added to user.txt!\n")
                add = False
#function called when a new task needs to be added
# information to add new tas will be saved to task.txt file  
def add_task():
    
      

    #Import packages for datetime
    import datetime
    from datetime import date
     #opening and appending  tasks.txt file
    task_files = open ( "tasks.txt" , "a") #open and append tasks.txt
    
    print("~"*132)
        
    print("\nTo add a task,please enter the following details:\n".upper())

    # getting  the appropriate information about task     
    username =input("Please enter the username of the person that you assigning the task to: ")
    task_title = input("Please enter the title of the task: ")
    description = input("Please enter the task description: ")
    date = date.today()
    due_date = input("Enter the due date for the task in this format(YYYY-MM-DD): ")
    completed = "No"
        
    add_task = "\n" + username + ", " + task_title + ", " + description + ", " + str(date) + ", " + due_date + ", " + completed
    
    # writing task information to task file
    task_files.write(add_task)

    print(f"\nyou have successfuly assigned a task to {username} in tasks.txt!\n".upper())
    #once information is added close task file
    task_files.close 
#this function is called all tasks have to be viewd
def view_all():

    # This function display the information for each task on the screen
    task_files = open ( "tasks.txt" , "r") #reopen and append tasks.txt
    task_lines = task_files.readlines()
    
    for number, line in enumerate (range(len(task_lines)), start= 0):
        task_line = task_lines[line].split(", ")
        print(f"Task {number} \nASSIGNED TO     : {task_line[0]} \nTASK            : {task_line[1]} \nTASK DESCRIPTION: {task_line[2]} \nDATE ASSIGNED   : {task_line[3]} \nDUE DATE        : {task_line[4]} \nTASK COMPLETED? : {task_line[5]}\n")
    #once tasks have been vied task file is closed
    task_files.close 
#this function is called when a user or admin wants to view their task
def view_mine():


    
    task_files = open ( "tasks.txt" , "r") #reopen and append tasks.txt
    task_lines = task_files.readlines()

    #program will search for the username in text files and print out their allocated tasks
    print (f"{username},the tasks assigned to you, are:\n")
    for num, line in enumerate (range(len(task_lines)), start = 0):
        task_line = task_lines[line].split(", ")
        if username == task_line[0]:
            print(f"Task {num} \nASSIGNED TO     : {task_line[0]} \nTASK            : {task_line[1]} \nTASK DESCRIPTION: {task_line[2]} \nDATE ASSIGNED   : {task_line[3]} \nDUE DATE        : {task_line[4]} \nTASK COMPLETED? : {task_line[5]}\n")
    
    task_files.close 
        
    edit = False
    while edit == False: 
        # choosin to mark task as complete or to edit task
        task_number = int(input("Please enter a task number to edit a task or -1 for main menu: "))

        # -1 is to allow user to return to main menu
        if task_number == -1:
            edit = True    

        else:
            task_file = open ('tasks.txt', 'r')
            # if the user chooses to mark their task complete, a list to store tasks is created
            # then we use number to get to that specific task 
            registry = []
            registry = task_file.read().splitlines()
            my_list_items = registry[task_number].split(", ") # selecting the task to be marked as complete so that we can edit item task complete
            
            mark_or_edit = input ("\nDo you want to mark this task as complete or edit? (enter 'c' or 'e')\n")
            # if option is c  to mark the task complete, 'Yes' is entered in that line of task to signify that the task has been completed
            if mark_or_edit.lower() == "c":
                my_list_items[5] = 'Yes'
                
                # after entering 'Yes', the line is joined back as it was originally in the list
                my_list_join = ", ".join(my_list_items)
                
                # after joining the line, we put it back into the tasks list at the very same position
                registry[task_number] = my_list_join
                
                # lastly write the whole list back in the text file
                task_file = open ('tasks.txt', 'w')
                for item in registry:
                    task_file.write(f"{item}\n")
                task_file.close
                print(f"\nTask {task_number} marked as complete!".upper())
                edit = True

            # if option is e to edit the task, if the task has already been marked as complete, user is notified that the task cannot be edited.
            elif mark_or_edit.lower() == 'e':
                if my_list_items[5] == 'Yes':
                    print(f"\nTask {task_number} has already been completed, you cannot edit it\n".upper())
                else:
                    # if the username can edit the task, user is asked what they want to add which can only be either the username or the due date
                    # once choice is made, the same logic used above is applied. We take the specific line in the task list where the changes have to be made
                    # then we can change either the username or the due date, then we join the line back to its original form and put it back in the tasks list with the changes made.
                    option = input ("Enter (u) to edit username or (d) to edit the task due date: ")
                    if option.lower() == "u":
                        change_username = input("\nEnter the new username: ")
                        my_list_items[0] = change_username
                        my_list_join = ", ".join(my_list_items)
                        registry[task_number] = my_list_join
                        #printing my list
                        task_file2 = open ('tasks.txt', 'w')
                        for item in registry:
                            task_file2.write(f"{item}\n")
                        task_file2.close()
                        print(f"\nTask {task_number} is now assigned to {change_username}\n")

                    elif option.lower() == "d":
                        modifying_date = input ("Enter the new due date (YYYY-MM-DD): ")
                        my_list_items[4] = modifying_date
                        my_list_join = ", ".join(my_list_items)
                        registry[task_number] = my_list_join
                        
                        task_file3 = open ('tasks.txt', 'w')
                        for component in registry:
                            task_file3.write(f"{component}\n")
                        task_file3.close
                        print (f"\nThe new due date for Task {task_number} is {modifying_date}\n")
                        break 
            
            task_file.close()
#this function is called when admin wants to generate reports
#these reprts are written to task_overview.txt and user_overview.txt file
def reports():

    

    #Import packages
    import datetime
    from datetime import date

    # reading tasks forom our task file
    reading_task3 = open ('tasks.txt', 'r')
    task_count = reading_task3.read().splitlines()
    reading_task3.close()
    list_len = len(task_count)
    print(f"Total tasks is {list_len}")

    #counters to count the number of tasks done, incomplete and overdue
    complete = 0
    incomplete = 0
    overdue = 0
    today = date.today() # stores the current date

    # counting the number of tasks completed and tasks that are incomplete
    for line in task_count:
        if "Yes" in line:
            complete +=1
        else:
            incomplete +=1
    

    # checking to see which tasks are overdue according to the current date adn due date
    for item in task_count:
        due_date = item.split(", ")[4]
        month = due_date[5:7]
        year = due_date[0:4]
        date_day = due_date[8::]

        # creating the due date into a date format
        due_date_int = date(int(year), int(month), int(date_day))

        # comparing the dates to determine if the task is overdue
        if due_date_int < today and "No" in item:
            overdue +=1
    
    # calculating the percentage of incomplete tasks a
    percentage_incomplete = (incomplete/list_len) * 100
    #calculating overdue tasks
    percentage_overdue = (overdue/list_len) * 100
    

    # writing information to task.overview text file
    outfile = open('task_overview.txt', 'w')
    outfile.write(f'''The total number of tasks is {list_len}
      total number of completed tasks is {complete},
      total number of uncompleted tasks is {incomplete} 
      The total number of tasks that are overdue and uncompleted is {overdue} ,
      The percentage of incomplete tasks is {percentage_incomplete:.2f}% 
      The percentage of tasks that are overdue is {percentage_overdue:.2f}%
      ''')
    outfile.close()

    
    # writing to user.txt file using above logic. 
    open_overview = open ('user_overview.txt', 'w')
    line_out = ""

    
    users_file_read = open ('user.txt', 'r')
    list_of_users = users_file_read.read().splitlines()
    users_file_read.close()
    list_users_len = len(list_of_users)

    read_tasks = open ('tasks.txt', 'r')
    tasks_list = read_tasks.read().splitlines()
    tasks_list_len = len(tasks_list)
    read_tasks.close()
    

    user_tasks_count = 0
    user_completed = 0
    user_incomplete = 0
    user_overdue= 0
     #list stores the usernames so that we can display details for each username
    usernames = [] 
    user_tasks = []
    
    # for each username
    #  the number of tasks assigned to that user is displayed
    #  the percentage of tasks assigned to that user is displayed
    #  the percentage of tasks completed is displayed
    # uncompleted and overdue tasks are displayed
    for line in list_of_users:
        usernames.append(line.split(", ")[0])

    # writing  the total number of users and tasks.
    #  for each user, we find the total number of tasks, the percentage of tasks completed and uncompleted and overdue.
    # we do this by using use counters which are set to 0 above and incremented once a specific condition is met.
    open_overview.write(f"The total number of users is {list_users_len} and the total number of tasks is {tasks_list_len}\n")
    for username in usernames:
        for task in range(0, len(tasks_list)):
            due_date = tasks_list[task].split(", ")[4]
            date_month = due_date[5:7]
            date_year = due_date [0:4]
            date_day = due_date [8::]
            due_date_int1 = date(int(date_year), int(date_month), int(date_day))
            today = date.today()
            if f"{username}" in f"{tasks_list[task]}":
                user_tasks_count += 1
            if f"{username}" in f"{tasks_list[task]}" and "Yes" in f"{tasks_list[task]}":
                user_completed += 1
            if f"{username}" in f"{tasks_list[task]}" and "No" in f"{tasks_list[task]}":
                user_incomplete += 1
            if f"{username}" in f"{tasks_list[task]}" and "No" in f"{tasks_list[task]}" and due_date_int1 < today:
                user_overdue += 1
        user_tasks.append(username)
        user_tasks.append(user_tasks_count)
        user_task_perc = round((user_tasks_count/tasks_list_len)*100, 2)
        user_tasks.append(user_completed)
        user_completed_tasks_perc = round((user_completed/tasks_list_len)*100, 2)
        user_tasks.append(user_incomplete)
        user_incomplete_tasks_perc = round((user_incomplete/tasks_list_len)*100, 2)
        user_tasks.append(user_overdue)
        user_overdue_tasks_perc = round((user_overdue/tasks_list_len)*100, 2)
        # for each user, we write the  details in the user overview text file
        line_out = username + " " + "has" + " " + str(user_tasks_count) + " tasks, " + str(user_task_perc) + "%" + " of tasks, " + " " + str(user_completed_tasks_perc) + "%" + " tasks completed" + ", " + str(user_incomplete_tasks_perc) + "%" + " incomplete tasks" + ", "+ str(user_overdue_tasks_perc) + "% " + " tasks overdue" + "\n"
        open_overview.write(line_out)
        # reseting the counters so that the calculations are done properly for each user.
        user_tasks_count = 0
        user_completed = 0
        user_incomplete = 0
        user_overdue = 0
    open_overview.close()
#this function is called when user wants to view statistics
def view_statistics():

    option = input ("\nPlease enter what you want to see 'users overview' or 'tasks overview'(enter 'u' or 't') ")
    # when admin chooses users overview, a list is created  to store all the lines in the file users_overview.txt.
    # then the reports read from the text file is printed to the user .
    if option.lower() == "u":
        user_overview = open ('user_overview.txt', 'r')
        user_overview_list = user_overview.read().splitlines()
        user_overview.close()
        for first_line in user_overview_list:
            print(first_line)      

    # when the user chooses tasks overview,  a list is created containing all the  details from the text file.      
    elif option.lower() == "t":
        task_overview = open('task_overview.txt', 'r')
        task_overview_list = task_overview.read().splitlines()
        task_overview.close()
        for the_line in task_overview_list:
            print(the_line)

user_file = open ( "user.txt" , "r")

#the user must enter a username and password.
print("~"*132)

print("ENTER YOUR LOGIN DETAILS:")

print()

username=input("USERNAME: ")
password=input("PASSWORD: ")

#for loop to verify if the login details entered by the user are valid and registered in the user.txt file
correct= False

# loop through each line in the user.txt file and store each line in a list
for line in user_file:
    
    line = line.strip()
    details = line.split(", ")

    if username == details[0] and password == details[1]:
        accurate = False
        break
    else:
        accurate = True

while accurate:
    user_file.close()
    user_file= open ( "user.txt" , "r+")
    #Display  error message if the user enters a username that is not listed in user.txt or enters a valid username but not a valid password
    print("Username or password is incorrect,please enter the correct username and password!\n")
        
    #The user should repeatedly be asked to enter a valid username and password until they provide appropriate credentials.
    username=input("USERNAME: ")
    password=input("PASSWORD: ")
    accurate= False
    
    for line in user_file:
    #remove \n in each line
        line = line.strip()
        details = line.split(", ")

        if username == details[0] and password == details[1]:
            accurate = False
            break
        else:
            accurate = True

print("~"*132)
print(f"\nwelcome {username}, you have successfully logged in.\n".upper())

#while username is not admin
while username != "admin":
    print("~"*132)
    # display a menu once a user have successfully logged in
    user_menu = input('''PLEASE SELECT ANY OF THE FOLLOWING: 
    a - add task 
    va - view all tasks 
    vm - view my tasks 
    e - exit 
    ''')
    print()

    # If the user chooses a to register a user, the function reg_user() must be called.
    if user_menu.lower()=="r":
        print("~"*132)
        reg_user()

    # If the user chooses a to register a user, the function add_task() must be called.
    if user_menu.lower()=="a":
        print("~"*132)
        add_task()
        
    #If the user chooses va to view all tasks, the function view_all() must be called.
    if user_menu.lower()=="va":
        print("~"*132)
        view_all()
   
    #If the user chooses vm to view all tasks, the function view_mine() must be called.
    if user_menu.lower()=="vm":
        print("~"*132)
        view_mine()
            
    if user_menu.lower()=="e":
        print("\nTHANK YOU FOR LOGGING IN\n")
        break

#while the logged in user is the admin   
while username == "admin": 
    print("~"*132) 

    # display a new menu that includes viewing stats
    admin_menu=input('''PLEASE SELECT ANY OF THE FOLLOWING:
    r - register user 
    a - add task 
    va - view all tasks 
    vm - view my tasks 
    gr - generate reports 
    vs - view statistics of tasks and users 
    e - exit 
    ''')
    print()
    
    # If the user chooses r to register a user, the function reg_user() must be called.
    if admin_menu.lower() == "r":
        print("~"*132)
        reg_user()
    
    # If the user chooses a to register a user, the function add_task() must be called.    
    if admin_menu.lower() == "a":
        print("~"*132)
        add_task()

    #If the user chooses va to view all tasks, the function view_all() must be called. 
    if admin_menu.lower() =="va":
        print("~"*132)
        view_all()
    
    #If the user chooses  to view all tasks, the function view_mine() must be called.
    if admin_menu.lower() =="vm":
        print("~"*132)
        view_mine()

    # if the user chooses to generate reports, two text files, called task_overview.txt and user_overview.txt , should be generated
    if admin_menu.lower() =="gr":
        print("~"*132)
        reports()

        print("Reports generated. Please check 'task_overview.txt' and 'user_overview.txt' to see them.\n")

    #for admin to view the statistics of the task if needed
    if admin_menu.lower() == "vs":
        
        print("~"*132)
        generate_stats = input("To view statistics,please enter 'gr' to genarate stats firts: ")

        if generate_stats == "gr":
            reports()

        print("Reports generated.\n")

        view_statistics()

    
    if admin_menu.lower()=="e":
        print("\nthank you for logging in\n")
        break

#close both user and task files
user_file.close()