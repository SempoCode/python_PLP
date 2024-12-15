class Animal:
    def __init__(self, no_of_legs):
        self.no_of_legs = no_of_legs

    def move(self):
        print("an animal moves")

class Human(Animal):
    def __init__(self, no_of_legs = 2):
        super().__init__(no_of_legs)

    def move(self):
        print("A person walks")

class Bird(Animal):
    def __init__(self, no_of_legs = 2):
        super().__init__(no_of_legs)

    def move(self):
        print("A bird flies")

class Snake(Animal):
    def __init__(self, no_of_legs = 0):
        super().__init__(no_of_legs)

    def move(self):
        print("A snake crawls")

class Cow(Animal):
    def __init__(self, no_of_legs = 4):
        super().__init__(no_of_legs)

    def move(self):
        print("A cow walks")


man = Human()
print(f"\nA person has {man.no_of_legs} legs")
man.move()

eagle = Bird()
print(f"\nA bird has {eagle.no_of_legs} legs")
eagle.move()

cobra = Snake()
print(f"\nA snake has {cobra.no_of_legs} legs")
cobra.move()

cow = Cow()
print(f"\nA cow has {cow.no_of_legs} legs")
cow.move()
