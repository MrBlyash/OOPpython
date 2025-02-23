import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car and self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()

    def get_pet(self):
        self.pet = Pet()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car and self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
        else:
            if self.car and self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()

    def shopping(self, manage):
        if self.car and self.car.drive():
            pass
        else:
            if self.car and self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def play_with_pet(self):
        if self.pet:
            print("Playing with my pet!")
            self.gladness += 15
            self.pet.happiness += 10
        else:
            print("I don't have a pet!")

    def feed_pet(self):
        if self.pet:
            if self.home.food > 5:
                print("Feeding my pet!")
                self.pet.hunger -= 10
                self.home.food -= 5
            else:
                print("Not enough food to feed my pet!")
        else:
            print("I don't have a pet!")

    def live(self, day):
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I got a job as a {self.job.job} with salary {self.job.salary}")
        if self.pet is None:
            self.get_pet()
            print("I got a pet!")

        print(f"\nDay {day}: {self.name}'s Life")
        print(f"Money: {self.money}, Satiety: {self.satiety}, Gladness: {self.gladness}")
        print(f"Car Fuel: {self.car.fuel}, Car Strength: {self.car.strength}")

        dice = random.randint(1, 6)
        if self.satiety < 20:
            print("I'm hungry, I'll eat.")
            self.eat()
        elif self.gladness < 20:
            print("I'm feeling sad, I'll play with my pet.")
            self.play_with_pet()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Start working!")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping("delicacies")
        elif dice == 5:
            print("Playing with pet!")
            self.play_with_pet()
        elif dice == 6:
            print("Feeding my pet!")
            self.feed_pet()


class Pet:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


nick = Human(name="Nick")
for day in range(1,800):
    if nick.live(day) == False:
        break