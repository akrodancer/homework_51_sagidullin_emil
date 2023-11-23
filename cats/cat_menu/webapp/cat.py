from random import randint


class Cat:
    def __init__(self, name, food=40, mood=40, age=1, state=True):
        self.name = name
        self.food = food
        self.mood = mood
        self.age = age
        self.state = state
        if 1 <= self.mood <= 33:
            self.img = "img/cat1.jpg"
        elif 34 <= self.mood <= 66:
            self.img = "img/cat2.jpeg"
        elif 64 <= self.mood <= 100:
            self.img = "img/cat3.jpeg"

    def feed(self):
        self.food += 15
        self.mood += 5

    def play(self):
        choice = randint(1, 3)
        if choice == 1:
            self.state = True
            self.mood = 0
        else:
            if self.state == True:
                self.mood += 15
                self.food -= 10
            elif self.state == False:
                self.state = True
                self.mood -= 5

    def change_state(self):
        if self.state == True:
            self.state = False
        elif self.state == False:
            self.state = True





