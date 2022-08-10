# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
#              Allow user to display, add, or remove rows from the table
#              Save the table contents to ToDoList.txt if desired
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# jtlarson,2022-08-08,Added code to complete assignment 5
# jtlarson,2022-08-09,Added strip and replace methods to filter input;
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""   # A row of text data from the file
lstRow = []   # A row of data split into a list based on comma-separated value formatting
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
intTaskNameLength = 0 #store the length of the task name

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# File to List
#Using 'try, except' to provide enhanced suggestions if loading any rows from file fails
try:
    objOpenFile = open(objFile, "r") #open file in read mode
    print("Loading 'ToDoList.txt' file contents...")
    for strData in objOpenFile: #iterate through lines of file
        lstRow = strData.split(",") # Returns a list from CSV formated data
        dictRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()} #assign list items to dictionary values
        lstTable.append(dictRow) #append dictionary to table list
    objOpenFile.close() #close file for now
except: #print helpful error message and exit if anything in the try block fails
    print("Unable to retrieve data from ToDoList.txt. Confirm file exists, with rows in 'task,priority' (CSV) format")
    exit()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        intTaskNameLength = 0 #store the length of the task name
        #Find the longest task name, and print the column headers to fit
        for row in lstTable:
            if len(row['Task']) > intTaskNameLength:
                intTaskNameLength = len(row['Task'])
        print("Task", " " * (intTaskNameLength - 4), "|", "Priority")
        #Print each row with the same column width as the header
        for row in lstTable:
            print(row['Task'], " " * (intTaskNameLength - len(row['Task'])), "|", row['Priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Ask user for task and priority, then store these entries in dict
        strTaskName = input("What task do you want to add?: ").strip()
        strTaskPriority = str(input("What priority is this task?: ").strip()) #store as a string
        dictRow = {'Task': strTaskName.replace(","," "), 'Priority': strTaskPriority.replace(","," ")}
        #append dict as new row to existing list table
        lstTable.append(dictRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        intTaskNameLength = 0 #store the length of the task name
        #Find the longest task name
        for row in lstTable:
            if len(row['Task']) > intTaskNameLength:
                intTaskNameLength = len(row['Task'])
        # Display indexed list of records to delete
        intRowCount = 0
        for row in lstTable:
            print(intRowCount, ":", row['Task'], " " * (intTaskNameLength - len(row['Task'])), "|", row['Priority'])
            intRowCount += 1
        intRowDelete = int(input("Enter the index number of the row you want to remove: "))
        #pop method returns the value being removed
        if intRowDelete < intRowCount:
            print("Deleting: ", lstTable.pop(intRowDelete))
        else:
            print("Record not found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # Open the file in write mode
        objOpenFile = open(objFile, "w")
        #Iterate through the dictionaries and write the key:value pairs to the file in CSV
        for dictRow in lstTable:
            objOpenFile.write(dictRow["Task"] + ',' + dictRow["Priority"] + '\n')
        print("Saving data...")
        objOpenFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # Exit message
        print("Exiting program...")
        break  # and Exit the program
