# -*- coding: UTF-8 -*-
class Animal(object):
    def run(self):
        print("animal is running...")

class Dog(Animal):
    def run(self):
        print("dog is running...")

class Cat(Animal):
    def run(self):
        print("cat is running...")

def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?',isinstance(a,Animal))
print('a is Dog?',isinstance(a,Dog))
print('a is Cat?',isinstance(a,Cat))

print('d is Animal?',isinstance(d,Animal))
print('d is Dog?',isinstance(d,Dog))
print('d is Cat?',isinstance(d,Cat))

run_twice(c)
run_twice(a)