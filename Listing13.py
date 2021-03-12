# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# <Your Name>,<Today's Date>,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# Main Body of Script  ---------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

print(Eio.print_menu_items())

choice = Eio.input_menu_options()
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable = []
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))


while(True):
    if choice == "1":
        print(Eio.print_current_list_items(lstTable))
        print(Eio.print_menu_items())
        choice = Eio.input_menu_options()

    if choice == "2":
        lstTable.append(Eio.input_employee_data())
        print(Eio.print_menu_items())
        choice = Eio.input_menu_options()
    if choice == "3": 
        Fp.save_data_to_file("EmployeeData.txt", lstTable)
        print("File Saved!")
        choice = Eio.input_menu_options()
    if choice == "4":
        print("Exiting.... have a nice day")
        break



