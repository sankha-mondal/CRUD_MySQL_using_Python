import mysql.connector

conn = mysql.connector.connect(host='localhost', port='3306', database='mydb', user='root', password='#Sankha12@98')

print('=' * 40)
# Check the connectivity with MySQL -Db
if conn.is_connected():
    print("Connected to database")
print('=' * 40)

# ====== List Employees =====

def list_students():
    cursor_rd = conn.cursor()

    print('Fetch all rows')
    cursor_rd.execute('select * from employee')
    rows = cursor_rd.fetchall()
    print("Total rows returned: ", cursor_rd.rowcount)

    for row in rows:
        print(row)
    
    
# ====== Create Student =====

def create_employee(id, name, salary):
    strQ = "insert into employee (id, name, salary) values  ('"+id+"', '"+name+"', '"+salary+"')"
    # print(strQ)
    cursor_cr = conn.cursor()
    cursor_cr.execute(strQ)

    # print('Results of database operation: ', cursor_cr.rowcount)
    if cursor_cr.rowcount == 0:
        print("Employee = " + name + " not created")
    else:
        print("Employee = " + name + " created")
        conn.commit()
        
# ====== Update Employee =======

def update_employee():
    employee_to_update = input("Enter employee ID to update: ")
    find_string = " select * from employee where id = '" + employee_to_update + "'"

    cursor_up = conn.cursor()
    cursor_up.execute(find_string)

    rows = cursor_up.fetchall()
    print( "\n Employee record to be updated")

    for row in rows:
        print(row)

    iname, isalary = input(' To update record, enter Employee Name and Salary separated by a comma: ').split(',')
    update_string = "update employee  set name = '" + iname + "', salary = '" + isalary + "' where id = '" + employee_to_update + "'"
    #print ( update_string)

    cursor_up.execute(update_string)

    # print('Results of database operation: ', cursor_up.rowcount)

    if cursor_up.rowcount == 0:
        print("\n Employee = " + iname + " not updated")
    else:
        print("\n Employee = " + iname + " update")
        conn.commit()
        
        
# ====== Delete Employee =====

def delete_employee():
    employee_to_delete = input("Enter Employee Id to delete: ")
    str = "delete from employee where id='" + employee_to_delete + "'"

    cursor_de = conn.cursor()
    cursor_de.execute(str)

    print('Results of database operation: ', cursor_de.rowcount)
    if cursor_de.rowcount == 0:
        print("Employee with ID = " + employee_to_delete + " not deleted")
    else:
        print("Employee with ID = " + employee_to_delete + " deleted")
        conn.commit()


def menu():
    # Setup Menu Choices --------
    Menu_Items = {'1': 'List of Employees', '2': 'Add new Employee data', '3': 'Update Employees data', '4': 'Delete Employees data', '5': 'Exit'}
    Valid_Choice = {1, 2, 3, 4, 5}

    # Display Menu ----------
    print('\n  Employees Management System:')
    print('-------------------------------------------------------------------')
    print('\n  Menu Items:')
    print(' Select menu item. ')

    MenuSelected = 0

    r = range(1, (len(Menu_Items) + 1), 1)
    for i in r:
        MenuItem = Menu_Items.__getitem__(str(i))
        print('  ', i, '  ', MenuItem)

    MenuSelected = int(input(' Menu number: '))

    while MenuSelected not in Valid_Choice:
        print("Menu item not valid.  Please choose option")
        print('\n Select menu item. ')
        MenuSelected = int(input('\n Menu number: '))


    # ===== Mainline =====
    print(MenuSelected)
    if MenuSelected == 1:
        list_students()

    if MenuSelected == 2:
        id = ''
        i_name = ''
        i_salary = ''
        n = 0
        while n < 10:
            id = input (' Enter Employee Id ( or exit to finish): ')
            if id == 'exit':
                menu()
            i_name  = input (' Enter Employee Name: ')
            i_salary = input(' Enter Employee Salary : ')

            create_employee(id, i_name, i_salary )

    if MenuSelected == 3:
        list_students()
        update_employee()


    if MenuSelected == 4:
        list_students()
        delete_employee()

    if MenuSelected == 5:
        exit()

if __name__ == "__main__":
    menu()
    
conn.close()

# ==========================================================================================================
