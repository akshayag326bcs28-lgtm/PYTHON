class Animal:
    def speak(self):
        print("Generic animal sound")

class Bird(Animal):
    def speak(self):
        print("Tweet")
my_bird = Bird()
my_bird.speak()
