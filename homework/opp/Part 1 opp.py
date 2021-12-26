# 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


my_car = Vehicle(max_speed=130, mileage=250)
print(my_car)


# 2
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity
    def print_seating_capacity(self):
        pass


bus1 = Bus(120, 450, 25)

# 3
print(type(bus1))

# 4
school_bus = Bus(125, 800, 35)
print(isinstance(school_bus, Vehicle))


# 5
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_student = number_of_students


# 6
class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, capacity, bus_school_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, capacity)
        self.bus_school_color = bus_school_color
    def print_bus_school_color(self):
        pass


# 7
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return (f"Bear says {self.sound}")


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return (f"Wolf says {self.sound}")


bear = Bear('rrr')
wolf = Wolf('auu')
Animals = (bear, wolf)
for sound in Animals:
    print(sound.make_sound())

# 8
class City():

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __call__(self):
        if  self.population >= 1500:
            return self.name
        else:
            return (f'Your city is too small')

My_City = City('Lviv', 1976)
print(My_City.__call__())