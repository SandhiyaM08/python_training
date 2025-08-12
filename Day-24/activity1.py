#activity01

#create an abstract class animal with speak method ,implement dog and cat

from abc import ABC,abstractmethod
class Animal(ABC):
	@abstractmethod
	def speak(self):
		pass
class Dog(Animal):
	def speak(self):
		print("Barking")
class Cat(Animal):
	def speak(self):
		print("Meow")
def main():
    dog = Dog()
    cat = Cat()

    dog.speak()
    cat.speak()

if __name__ == "__main__":
    main()




