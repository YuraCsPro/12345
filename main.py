import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.thirst = 100
    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety == 100
                return
            self.satiety += 5
            self.home.food -= 5

    def drink(self):
        if self.home.water <= 0:
            self.shopping("water")
            self.thirst -= 20
            self.home.water -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                self.shopping("fuel")
                return

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 5
        self.thirst -= 2


    def shoping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel!")
            self.money -= 100
            self.car.fuel == 100
        elif manage == "food":
            self.money -= 50
            self.home.food += 50
        elif manage == "water":
            self.money -= 5
            self.home.water += 5
        elif manage == "delicatese":
            print("Im happy!")
            self.gladness += 10
            self.money -= 5
            self.satiety += 2

    def chill(self):
        pass

    def clean_Home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self, day):
        d = f"Today the {day} of {self.name}'s indexes"
        print(f"{d:=^50}")
        human_i = f"{self.name}'s indexes"
        print(f"{human_i:=^50}")
        print(f"Home indexes:=^50")

        car_i = f"{self.car.brand} car indexes"
        print(f"{car_i:=^50}")
        print(f"Fuel: {self.car.fuel}")
        print(f"strength: {self.car.strength}")


    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        elif self.satiety < 0 or self.thirst < 0:
            print("Dead...")
            return False
        elif self.money < -100:
            print("Bankrupt...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settle in house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I working {self.job.job}, salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety < 10:
            print("Time to eat!!!")
            self.eat()
        elif self.gladness < 5:
            print("Time to chill!")
        elif self.money < 5:
            print("Time to Working!")
            self.work()
        elif self.car.strength < 10:
            print("Time to repair car!")
            self.to_repair()
        elif dice == 1:
            print("Lets Chill")
            self.chill()
        elif dice == 2:
            print("Lets Working!")
        elif dice == 3:
            print("Lets Cleaning home")
            self.clean_Home()
        elif dice == 4:
            manage = "delicatese"
            self.shopping(manage)

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The Car cannot move!")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.water = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {"Python developer": {"salary": 50, "gladness_less": 12},
        "C++ developer": {"salary": 70, "gladness_less": 6},
        "Php developer": {"salary": 30, "gladness_less": 4}}

brands_of_car = {"Bmw_M5_F90": {"fuel": 25, "strength": 80, "consumption": 14},
                 "Nissan_Skyline_R34": {"fuel": 50, "strength": 110, "consumption": 20},
                 "Bugatti_Chiron": {"fuel": 100, "strength": 140, "consumption": 30},
                 "BMW_M4_F82": {"fuel": 100, "strength": 75, "consumption": 17}}


nick = Human("Nick")
for day in range(1, 8):
    if nick.live(day) == False:
        break

