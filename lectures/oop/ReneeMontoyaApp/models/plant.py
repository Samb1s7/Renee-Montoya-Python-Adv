from lectures.oop.ReneeMontoyaApp.framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, id, location, name, director_id):
        self.id = id
        self.location = location
        self.name = name
        self.director_id = director_id

Plant.save
Plant._generate_dict
