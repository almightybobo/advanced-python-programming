# Prime Numbers Iterators

We're going to increase the complexity of our iterators practice by building an Iterator that returns only Prime Numbers. Before jumping to the Iterator itself, we've made a decision about how the object should check if a number is prime. The `PrimeNumbersIterator` has a `_is_prime(num)` method that accepts a natural number and returns `True` or `False` depending if it's prime or not. Example:

```python
obj = PrimeNumbersIterator()
obj._is_prime(3)  # True
obj._is_prime(199)  # True
obj._is_prime(20)  # False
```

This means that you'll be able to use the `_is_prime(num)` method inside your `__next__` method.

Now, about that iterator. This is an example of how it should work:

```python
iterator = iter(PrimeNumbersIterator())

next(iterator)  # 2
next(iterator)  # 3
next(iterator)  # 5
next(iterator)  # 11
next(iterator)  # 13
# ... fast forward ...
next(iterator)  # 163
next(iterator)  # 167
next(iterator)  # 173
# Etc.
```
