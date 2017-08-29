# Advanced OOP Topics

Throughout this unit we'll be focusing on different OOP topics that are a little bit more advanced. They're not hard to understand, though, don't worry. We say they're "advanced" because they're not usually taught. We'll be learning about:

* Magic Methods
* Properties (or "Computed Attributes")
* Iterators

## Magic Methods

Magic methods will allow you to supercharge your own classes to support operators that seem native in Python. For example, you can "overload" the `+` operator to give your own class a special meaning:

Read more about Magic Methods here: [http://minhhh.github.io/posts/a-guide-to-pythons-magic-methods](http://minhhh.github.io/posts/a-guide-to-pythons-magic-methods).

## Properties (Computed Attributes)

Python Properties will let you "simulate" attributes for your objects. Consider the following example:

```python
d = Distance(meters=8000)

print(d.distance_in_meters)     # 8000
print(d.distance_in_feet)       # 26246
print(d.distance_in_kilometers) # 8
print(d.distance_in_miles)      # 5
```

How would you approach the problem above? A big `__init__` method with all the values precomputed? It's probably not worth it. For example, if the `distance_in_miles` is seldom used, and you're creating millions of `Distance` objects, then you're wasting precious processing time for a value that won't be used that much. So, **how do we approach solving this issue?**. The answer is "computed attributes", or **properties**. A Python property is a special type of method that is _defined_ as a method, but it's invoked as an _attribute_ 🤔. Sounds weird, but it's actually really simple. Example:

```python
class Number(object):
    def __init__(self, value):
        self.value = value

    @property
    def doubled(self):
        return self.value * 2

    @property
    def tripled(self):
        return self.value * 3


one = Number(1)
five = Number(5)

print(one.doubled)  # 2
print(one.tripled)  # 3

print(five.doubled) # 10
print(five.tripled) # 15
```

In this example, we're referencing `doubled` or `tripled` as an attribute (without parentheses), but it's actually defined as a method. So this method, is just simulating the _get_ operation from an attribute. It's also possible to simulate a _set_ operation. Example:

```python
class Number(object):
    def __init__(self, value):
        self.value = value

    @property
    def doubled(self):
        return self.value * 2

    @doubled.setter
    def doubled(self, doubled_value):
        self.value = doubled_value / 2

    @property
    def tripled(self):
        return self.value * 3

    @tripled.setter
    def tripled(self, tripled_value):
        self.value = tripled_value / 3

a_number = Number(2)

a_number.doubled = 8  # Setting the value
print(a_number.value)

a_number.tripled = 9  # Setting the value
print(a_number.value)
```

By using the `[METHOD].setter` decorator we can simulate that we're setting an attribute but we're actually just computing a function that can run any arbitrary code that we want.

Read more about properties here: [http://stackabuse.com/python-properties/](http://stackabuse.com/python-properties/).
