class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError()


class Cat(Animal):
    # def __init__(self, name):
    #     super(Cat, self).__init__(name)

    def talk(self):
        return 'meow'


class Dog(Animal):
    # def __init__(self, name):
    #     super(Dog, self).__init__(name)

    def talk(self):
        return 'woof'

if __name__ == '__main__':
    garfield = Cat(name='Garfield')
    odie = Dog(name='Odie')

    print(garfield.name)  # 'Garfield'
    print(odie.name)      # 'Odie'

    print(garfield.talk())  # 'meow'
    print(odie.talk())      # 'woof'
