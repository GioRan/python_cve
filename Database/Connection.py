import mysql.connector

class DatabaseConnection:

    def __init__(self):
        configuration = {
            'user': 'root',
            'password': 'GioRan12!',
            'host': '127.0.0.1',
            'database': 'person',
            'raise_on_warnings': True
        }

        try:
            self.connection = mysql.connector.connect(**configuration)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def closeConnection(self):
        self.connection.close()
