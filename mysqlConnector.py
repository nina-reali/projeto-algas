import mysql.connector

class Connector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connection(self):
        print("\nConecting, please hold...")
        try:
            mydb = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print("Conected\n")
            return mydb
        except Exception as e:
            print(e)
            self.shut_down("There has been an error connecting, connection closed.")

    def insert(self, values, table):
        mydb = Connector.connection(self)
        insert = mydb.cursor()
        query = "INSERT INTO {} (field_time, field_memory, field_end, field_start, field_gap, field_transaction) VALUES (%s, %s, %s, %s, %s, %s)".format(table)

        if not values:
            self.shut_down("Empty data")

        try:
            insert_value = (values['time'], values['memory'], values['start'], values['end'], values['gap'], values['transaction'])
            insert.execute(query, insert_value)
            mydb.commit()
            print("\nData registered\n")
        except Exception as e:
            print(e)
            self.shut_down("Error inserting data")

    def shut_down(self, message):
        print(message)
        from sys import exit
        exit(0)