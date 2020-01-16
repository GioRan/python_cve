
class PersonEntity:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def getPerson(self):
        person = {}
        person['name'] = self.name
        person['gender'] = self.gender

        return person