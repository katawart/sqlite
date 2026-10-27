import sqlite3 as sql

class sql_handling():

    cursor =  ""
    my_conn = ""

    #constructor: Takes on condition, a database to connect to.
    def __init__(self, database):

        #create the connection
        with sql.connect(database) as self.my_conn:
            print(self.my_conn)
            self.cursor = self.my_conn.cursor()
            

    #Preconditions: Takes a query that creates a table
    #Postconditions: A table is created
    def sql_make_tbl(self, query):
        try:
            self.cursor.execute(query) 
            self.my_conn.commit()
            return True
        except Exception: 
            return False
        

 
    #Preconditions Takes two values a query to run, vals to use.
    #Postcondition: Data in table is updated.
    def sql_insert(self, tbl, vals):
        vals = (vals[0], vals[1], vals[2])
        self.cursor.execute(f"INSERT INTO {tbl} VALUES (?, ?, ?)", vals)    
        self.my_conn.commit()    


    #Preconditions: Takes one value a query to run.
    #Postconditions: Returns x number of rows from a table.
    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    


    #Preconditions: Takes one value, a table to drop.
    #Postconditions: Table is dropped including all data.


    
if __name__ == "__main__":

    connector = sql_handling("students.db")
    #Checks to see if table already exists
    if not connector.sql_make_tbl("CREATE TABLE student (FIELDS name VARCHAR(20), class VARCHAR(20), course VARCHAR(20));"):
        connector.sql_insert("student", ["Richard", "1B","Computing"])
        rows = connector.fetch_all(f"SELECT * FROM student;")
        for row in rows:
            print (row)
        