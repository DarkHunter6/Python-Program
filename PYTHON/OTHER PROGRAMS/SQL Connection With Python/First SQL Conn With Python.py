import pyodbc # pyodbc Package Helps Us To Provide Any Functionality Of SQL Server

# Now Define The Connection String
SqlDbConn = pyodbc.connect("Driver={SQL Server};" "Server=DARKEAGLE\SQLEXPRESS;" "Database=School;" "Trusted_connection=yes;")

# # # # # # # #  Write Function For Show The Data From The Table # # # # # # # # 

# def Get_Data(SqlDbConn):
#     print('* * * Read Data From Students Table * * *')
#     print('')
#     Cursor = SqlDbConn.cursor()
#     # Cursor_2 = SqlDbConn.cursor()
#     # Cursor.execute("Select *From Students")
#     Query = "Select *From Students WHERE NAME=?" # Defend Database From SQL Injection Attacks
#     Parameters = ['Dark Hunter'] # We Pass The Data Into This Variable
    
#     # for Row in Cursor.execute("Select *From Students"):
#     for Row in Cursor.execute(Query, Parameters):
#         print(Row)
    
#     # print('Teachers')
#     # print('')
#     # for Row_2 in Cursor_2.execute("Select *From Teachers"):
#     #     print(Row_2)
        
# Get_Data(SqlDbConn)

# # # # # # # #  Write Function To Insert Data To The Table # # # # # # # # 

# def InsertData(SqlDbConn):
#     print(' * * * * * Insert Data Into The Table * * * * * ')
#     print()
#     # Name = input('Enter The Name : ')
#     # Address = input('Enter Your Address : ')

#     Cursor = SqlDbConn.cursor() # cursour Help  Us To Store The Table Rows
#     Cursor.execute("INSERT INTO Teachers(NAME, ADDRESS) VALUES('Suryokanto Mishra', 'Coochbehar')")
#     Cursor.commit()
    
#     Cursor_2 = SqlDbConn.cursor()
#     for Row in Cursor_2.execute("SELECT *FROM Teachers"):
#         print(Row)
        
# InsertData(SqlDbConn)