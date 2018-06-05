import sqlite3

class database:
    # Database 
    #
    def __init__(self):
        self.db_conn = sqlite3.connect('test.db')
        print("Database Created")
        # connect() will open an SQLite database, or if it
        # doesn't exist it will create it
        # The file appears in the same directory as this
        # Python file

 
        # A cursor is used to traverse the records of a result
        self.theCursor = self.db_conn.cursor()
        
    
    
    # ---------- FUNCTIONS ----------
    
    def printDB(self):
    # To retrieve data from a table use SELECT followed
    # by the items to retrieve and the table to
    # retrieve from
 
        try:
            result = self.theCursor.execute("SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")
 
            # You receive a list of lists that hold the result
            for row in result:
                print("ID :", row[0])
                print("FName :", row[1])
                print("LName :", row[2])
                print("Age :", row[3])
                print("Address :", row[4])
                print("Salary :", row[5])
                print("HireDate :", row[6])
                print()
        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")
 
        except:
            print("Couldn't Retrieve Data From Database")
 
# ---------- END OF FUNCTIONS ----------
    
 
    #Possible to create your own custom querty but you have to hard code it
    def addtodatabase(self, fname,lname,age,address,salary): 
        try:
            self.db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary,HireDate)" 
                                 "VALUES ('{}','{}',{},'{}','{}',date('now'))".format(fname,lname,age,address,salary) )
                                 
 
            self.db_conn.commit()
 
            print("Employee Entered")
 
        except sqlite3.OperationalError:
            print("Cant do add to the database")
            
        
 
        # You can update a value in a table by referencing
        # something unique like the ID or anything else
    # with the UPDATE command
    #Possible to create your own custom querty but you have to hard code it
    def editdatabase(self): 
        try:
            self.db_conn.execute("UPDATE Employees SET Address = '121 Main St' WHERE ID=2")
            self.db_conn.commit()
 
        except sqlite3.OperationalError:
            print("Database couldn't be Updated")
 
        
 
        # Delete matching data from the database by
    # referencing the table name and something unique
    #Possible to create your own custom querty but you have to hard code it
    def delete_index_by_ID(self,ID): 
        try:
            self.db_conn.execute("DELETE FROM Employees WHERE ID=" + str(ID))
            self.db_conn.commit()
 
        except sqlite3.OperationalError:
            print("Data couldn't be Deleted")
    #
    #Possible to create your own custom querty but you have to hard code it
    def createtable(self):   
        try:
            self.db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
 
            self.db_conn.commit()
 
            print("Table Created")
 
        except sqlite3.OperationalError:
            print("Table couldn't be Created")
    #Possible to create your own custom querty but you have to hard code it
    def deletetable(self):
        try:
            self.db_conn.execute("Drop TABLE Employees")
 
            self.db_conn.commit()
 
            print("deleted table complate")
 
        except sqlite3.OperationalError:
            print("cant delete the table from database")
 

 
def main():
    
    # first create a table
    db = database()
    #db.createtable()
    db.printDB()
    db.addtodatabase("john", "medel", 23, "623.elisa st.ny", '411,991')
    #delete by id
    db.delete_index_by_ID(2)
    
   


    
    
    
    
    
main()


