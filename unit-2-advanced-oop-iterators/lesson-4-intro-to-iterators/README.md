
Iterators are a fundamental concept in OOP. [Every](https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Iterators_and_Generators) [mature](https://docs.oracle.com/javase/7/docs/api/java/util/Iterator.html) [language](http://php.net/manual/en/class.iterator.php) will implement the iterator interface.

In this lesson, we talk about the importance of Iteration and the **Iterator Pattern**. You'll see how these two pieces are connected to finally use for loops on class with your instructor.

Here's a quick summary of the video.

## Iteration is key

Iteration provides a well known and intuitive interface to "loop" through things. Up to this point, you've always been used to iterate over collections:

```python
a_list = [1, 2, 3, 4]
for elem in a_list:
     print(elem)
```

But iteration is not restricted only to collections. For example, you can "iterate" a file line by line:

```python
f = open('records.csv')
for line in f:
     print(elem)
```

A `list` and a `file` are two **really** different type of objects; but yet, they support this intuitive interface.

Our objective is to build this interfaces into our own classes, so we can allow our users to _iterate_ over our own classes.

## Iterator Pattern - Usage

Before we can build these for-loops into our own classes, we need to understand the **_Iterator Pattern_**. This pattern is extremely simple. Let's see how we'd "use" it before we see how to implement it:

```python
a_list = ['Python', 'is', 'Awesome']
iterator = iter(a_list)

elem_1 = next(iterator)
print(elem_1) # Python

elem_2 = next(iterator)
print(elem_2) # is

elem_3 = next(iterator)
print(elem_3) # Awesome

# No more elements! What happens if we use next() again?
next(iterator)  # raises StopIteration() exception!
```

To _"use"_ the iterator pattern, we employ 2 functions: `iter()` and `next()`. `iter()` will be explained in class, so don't worry too much about that now. `next()` will ask for elements to the iterator and will receive one element at a time. When the iterator runs out of elements, invoking `next()` will raise a `StopIteration` exception.

## Iterator Pattern - Implementation

For a class to be considered an iterator it needs to support 2 methods: `__iter__` and `__next__` (`next` in Python 2). The `__iter__` method will be explained in class, so let's focus on the `__next__` method. `__next__` is the method that will be invoked whenever the `next()` function is applied on the iterator; so it needs just to return the element from the current iteration **or** raise a `StopIteration` exception if there are no more elements to iterate over.

## Optional Readings

If you're looking for external resources, you can check chapters [7](http://www.diveintopython3.net/iterators.html#a-fibonacci-iterator) and [8](http://www.diveintopython3.net/advanced-iterators.html) from [Dive into Python 3](http://getpython3.com/diveintopython3/index.html). They provide a good starting guide on Iterators.

If you have some 30 minutes available, I **highly** recommend Ned Batchelder's talk from PyCon 2013: [Loop like a native](https://www.youtube.com/watch?v=EnSu9hHGq5o).
