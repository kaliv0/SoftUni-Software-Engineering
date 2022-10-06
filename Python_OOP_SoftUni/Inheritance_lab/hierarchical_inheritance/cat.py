from animal import Animal
from dog import Dog


class Cat(Animal):
    @staticmethod
    def meow():
        return "meowing..."


if __name__ == '__main__':
    muttley = Dog
    bisou = Cat

    print("The dog is " + muttley.eat())
    print("The cat is " + bisou.eat())
    print('Tha cat is ' + bisou.meow())
    print('Tha dog is ' + muttley.bark())
