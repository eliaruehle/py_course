from car import Car
from person import Person

def main():
    car = Car("Audi A3", 2021, 5, 120)
    person1 = Person("Uwe", "Assmann", 50, "m")
    person2 = Person("Cristel", "Baier", 50, "f")
    person3 = Person("Ulrike", "Baumann", 55, "f")
    person4 = Person("Björn", "Andres", 40, "m")
    person5 = Person("Franz", "Baader", 60, "m")

    # test the print for persons:
    print(person1)
    # test the age getter:
    print(person1.get_age())
    # test birthday function:
    person1.has_birthday()
    print(person1.get_age())
    # test the age setter:
    person1.set_age(30)
    print(person1.get_age())
    # test mail registration:
    person1.register_mail("uwe.assman@tu-dresden.de")
    print(person1.get_mail())
    person2.get_mail()

    # testing the car:
    print(car)
    # add persons
    car.add_passenger(person1)
    print(car.get_passengers())
    car.add_multiple_passengers([person2, person3, person4, person5])
    print(car.get_passengers())
    assert(car.get_passengers() == ['Uwe Assmann', 'Cristel Baier', 'Ulrike Baumann', 'Björn Andres', 'Franz Baader'])
    car.start_ride()
    # remove persons
    car.remove_passenger(person1)
    print(car.get_passengers())
    car.start_ride()


if __name__ == "__main__":
    main()