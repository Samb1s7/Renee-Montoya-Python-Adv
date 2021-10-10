"""1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class"""

class Animals():

    def eat(self):
        print ("Eating")

    def sleep(self):
        print ("Sleaping")


class Tiger(Animals):

    def __init__(self, crawling, attack):

        self.attack_power = attack
        self.hunt = crawling

tiger = Tiger()

tiger.crawling
tiger.attack
tiger.eat()
tiger.sleep()

class Horse(Animals):

    def __init__(self, riding):

        self.riding = riding

    def run(self):
        pass
    def live_in_freedom(self):
        pass

horse = Horse()
horse.run
horse.riding
horse.eat()
horse.sleep()
horse.live_in_freedom()

class Cat(Animals):

    def __init__(self, meow, play):

        self.meow = meow
        self.crawling = play

cat = Cat()
cat.meow
cat.play
cat.sleep()
cat.eat()

class Dog(Animals):

    def __init__(self, guard, bark):

        self.guard = guard
        self.bark = bark

dog = Dog()
dog.guard
dog.bark
dog.sleep()
dog.eat()

class Bear(Animals):

    def __init__(self, hunt, fur):

        self.hunt = hunt
        self.fur = fur

bear = Bear()

bear.hunt
bear.hunt
bear.eat()
bear.sleep()

print(isinstance(tiger, Animals))
print(isinstance(horse, Animals))
print(isinstance(cat, Animals))
print(isinstance(dog, Animals))
print(isinstance(bear, Animals))

"""1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique."""

class Human():

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

    def study(self):
        print("Studying")

    def work(self):
        print("Working")

human = Human
human.sleep()
human.eat()
human.work()
human.study()


class Centaur(Human, Horse):

    def hunt(self):
        print ("Hunting")

centaur = Centaur
centaur.study()
centaur.eat()
centaur.run()
centaur.live_in_freedom()
centaur.work()

# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

class Person:

    def __init__(self, left_arm, right_arm):
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.arms = [left_arm, right_arm]


class Arm:

    def __init__(self, position):
        self.position = position


person = Person()
arm = Arm()


class Cellphone:
    def __init__(self, name):
        self.name = name


class Screen:
    def __init__(self, type):
        self.name = type


phone = Cellphone
screen = Screen

#  3. Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
#     Override a printable string representation of Profile class and return: list of the params mentioned above

class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __repr__(self):
        return f"Profile: name = {self.name}, last_name = {self.last_name}, phone_number = {self.phone_number}, address = {self.address}, email = {self.email}, birthday = {self.birthday}, age = {self.age}, sex = {self.sex}"

profile = Profile('Mark', 'Jason', '+123456789', 'some str 10','email@email.com', '12.12.1212', '12', 'male')
print(profile.__repr__)

# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import ABC, abstractmethod


@abstractmethod
class Interface(ABC):

    def screen(self):
        pass

    def keybord(self):
        pass

    def touchpad(self):
        pass

    def webcam(self):
        pass

    def ports(self):
        pass

    def dynamics(self):
        pass


class HPLaptop(Interface):

    def __init__(self, model):
        self.model = model

    def screen(self):
        print (f'{self.model}')

    def keybord(self):
        print (f'{self.model} includes eng and rus keyboards')

    def touchpad(self):
        print (f'{self.model} has a touchpad')

    def webcam(self):
        print (f'{self.model} has a webcam')

    def ports(self):
        print (f'{self.model} has some ports')

    def dynamics(self):
        print (f'{self.model} has dynamics')


hp = HPLaptop('hp_model')
hp.screen()
hp.keybord()
hp.touchpad()
hp.webcam()
hp.ports()
hp.dynamics()