# encoding: utf-8

# Animal是类,相同事物的统称
class Animal(object):
    def run(self):
        print('Animal is running...')


# Dog类,继承于Animal类
class Dog(Animal):
    pass

puppy = Dog()
puppy.run()

# 多态,子类方法覆盖父类方法
class Cat(Animal):
    def __init__(self, name):
        # __name是属性
        self.__name = name

    def getName(self):
        print(self.__name)

    def run(self):
        print('Cat is running...')


# limi是一个猫类的实例
limi = Cat("limi")
# run是实例的一个方法
limi.run()
# getName方法
limi.getName()
