# OOP (Object Oriented Programming)
#### Ref: https://reurl.cc/Vqy7Z
#### Ref: https://python.swaroopch.com/oop.html
#### Ref: https://python.swaroopch.com/exceptions.html

----
#### Fundamental of OOP
Main aspects: class & object
A class creates a new type where objects are instances of the class.
Ex. 'int' in python is also a class, help(int) can see more detail
Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as **fields**.
Objects can also have functionality by using functions that belong to a class. Such functions are called **methods** of the class.
The fields and methods can be referred to as the **attributes** of that class.
Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called **instance variables** and **class variables** respectively.

----
#### The 'self' ( strongly recommended to use it )
Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you **do not** give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name **self**.

----
#### The \_\_init\_\_ method
The \_\_init\_\_ method is run as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object. 

----
#### Class And Object Variables
**Class variables** are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.

**Object variables** are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance.

----
#### Inheritance
One of the major benefits of object oriented programming is **reuse** of code and one of the ways this is achieved is through the **inheritance** mechanism. Inheritance can be best imagined as implementing **a type and subtype relationship between classes**.

