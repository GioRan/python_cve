from Database.Connection import DatabaseConnection

class PersonService:

    def __init__(self):
        self.databaseConnection = DatabaseConnection()
        self.cursor = self.databaseConnection.connection.cursor()

    def savePerson(self, person):
        savePersonQuery = ("INSERT INTO "
                                "person "
                                "(person_name, person_gender) "
                            "VALUES "
                                "(%s, %s)")

        self.cursor.execute(savePersonQuery, (person['name'], person['gender']))
        self.databaseConnection.connection.commit()
        self.cursor.close()
        self.databaseConnection.closeConnection()
        
        
