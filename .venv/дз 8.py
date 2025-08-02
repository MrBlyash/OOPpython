import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True
        self.log_file = open("simulation_log.txt", "w", encoding="utf-8")
        self.log(f"Старт симуляції студента {self.name}")

    def log(self, message):
        self.log_file.write(message + "\n")
        print(message)

    def to_study(self):
        self.log("Time to study")
        self.progress += 0.15
        self.gladness -= 5

    def to_sleep(self):
        self.log("I will sleep")
        self.gladness += 3

    def to_chill(self):
        self.log("Rest time")
        self.gladness += 8
        self.progress -= 0.1
        self.money -= 10

    def to_work(self):
        self.log("Time to earn some money")
        self.money += 20
        self.gladness -= 4
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            self.log("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            self.log("Depression…")
            self.alive = False
        elif self.progress > 5:
            self.log("Passed externally…")
            self.alive = False
        elif self.money < -50:
            self.log("Bankruptcy…")
            self.alive = False

    def end_of_day(self):
        self.log(f"Gladness = {self.gladness}")
        self.log(f"Progress = {round(self.progress, 2)}")
        self.log(f"Money = {self.money}$")
        self.log("-" * 50)

    def automatic_decision(self):
        if self.money < 10:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.gladness < 30:
            self.to_chill()
        else:
            random.choice([self.to_study, self.to_sleep, self.to_chill])()

    def live(self, day):
        day_header = f"Day {day} of {self.name}'s life"
        self.log(f"{day_header:=^50}")
        self.automatic_decision()
        self.end_of_day()
        self.is_alive()
        if not self.alive:
            self.log(f"Simulation ended on day {day}.")
            self.log_file.close()

nick = Student(name="Nick")
for day in range(1, 366):
    if not nick.alive:
        break
    nick.live(day)
else:
    nick.log("Simulation completed: student survived all 365 days")
    nick.log_file.close()
