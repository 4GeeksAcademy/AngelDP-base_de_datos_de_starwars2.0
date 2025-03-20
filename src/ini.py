from app import app
from models import db, Planet, Specie, Vehicle, Starship, Person

with app.app_context():
    
    planets = [
    Planet(population=200000, climate="arid",
           terrain="desert", diameter=10465, gravity=1.0, name="Tatooine"),
    Planet(population=100000000, climate="temperate",
           terrain="urban", diameter=12240, gravity=1.0, name="Coruscant"),
    Planet(population=0, climate="frozen",
           terrain="tundra", diameter=7200, gravity=1.1, name="Hoth"),
    Planet(population=30000000, climate="temperate",
           terrain="forests, mountains", diameter=4900, gravity=0.85, name="Endor"),
    Planet(population=20000, climate="hot",
           terrain="volcanic", diameter=4200, gravity=1.2, name="Mustafar")
    ]
    if not Planet.query.first():
        db.session.add_all(planets)
        db.session.commit()


    species = [
    Specie(name="Human", height=1.75, hair_color="varied",
            skin_color="varied", language="Galactic Basic", average_life=100),
    Specie(name="Wookiee", height=2.2, hair_color="brown",
            skin_color="brown", language="Shyriiwook", average_life=400),
    Specie(name="Twi'lek", height=1.8, hair_color="varied",
            skin_color="blue, green, red, yellow", language="Twi'leki", average_life=85),
    Specie(name="Rodian", height=1.7, hair_color="none",
            skin_color="green", language="Rodese", average_life=70),
    Specie(name="Mon Calamari", height=1.6, hair_color="none",
            skin_color="orange, red", language="Mon Calamarian", average_life=80)
    ]
    if not Specie.query.first():
        db.session.add_all(species)
        db.session.commit()

    
    vehicles = [
    Vehicle(name="X-wing", crew=1, passengers=0, 
            class_name="Starfighter", cargo_cap=110, consumable="1 week"),
    Vehicle(name="TIE Fighter", crew=1, passengers=0, 
            class_name="Starfighter", cargo_cap=65, consumable="2 days"),
    Vehicle(name="Millennium Falcon", crew=4, passengers=6, 
            class_name="Light Freighter", cargo_cap=100000, consumable="2 months"),
    Vehicle(name="AT-AT", crew=5, passengers=40, 
            class_name="Walker", cargo_cap=1000, consumable="1 week"),
    Vehicle(name="Speeder Bike", crew=1, passengers=1, 
            class_name="Speeder", cargo_cap=20, consumable="1 day")
    ]   
    if not Vehicle.query.first():
        db.session.add_all(vehicles)
        db.session.commit()

    
    starships = [
    Starship(name="X-wing", crew=1, passengers=0, 
             class_name="Starfighter", cargo_cap=110, consumable="1 week"),
    Starship(name="TIE Fighter", crew=1, passengers=0, 
             class_name="Starfighter", cargo_cap=65, consumable="2 days"),
    Starship(name="Millennium Falcon", crew=4, passengers=6, 
             class_name="Light Freighter", cargo_cap=100000, consumable="2 months"),
    Starship(name="Star Destroyer", crew=47060, passengers=0, 
             class_name="Capital Ship", cargo_cap=36000000, consumable="2 years"),
    Starship(name="Slave I", crew=1, passengers=6, 
             class_name="Patrol Ship", cargo_cap=70000, consumable="1 month")
    ]
    if not Starship.query.first():
        db.session.add_all(starships)
        db.session.commit()


    people = [
    Person(name="Luke Skywalker", height=1.72, hair_color="Blond", 
           skin_color="Fair", eye_color="Blue", gender="Male"),
    Person(name="Darth Vader", height=2.03, hair_color="None", 
           skin_color="Pale", eye_color="Yellow", gender="Male"),
    Person(name="Leia Organa", height=1.50, hair_color="Brown", 
           skin_color="Fair", eye_color="Brown", gender="Female"),
    Person(name="Yoda", height=0.66, hair_color="White", 
           skin_color="Green", eye_color="Brown", gender="Male"),
    Person(name="Chewbacca", height=2.28, hair_color="Brown", 
           skin_color="Brown", eye_color="Blue", gender="Male")
    ]
    if not Person.query.first():
        db.session.add_all(people)
        db.session.commit()


print("initialized database")
