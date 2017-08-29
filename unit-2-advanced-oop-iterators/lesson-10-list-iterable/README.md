# List Iterable

Following our previous assignment, the objetive of this one is to split the _iterator_ from the _iterable_. You should be able to use your previous implementation for the iterable (you can actually copy and paste the code, removing the `__iter__` part). Example:


```python
iterator = ListIterator([3, 2, 1])

for elem in iterator:
    print(elem)
# Prints: 3, 2, 1

print("===============")

for elem in iterator:
    print(elem)
# Prints: 3, 2, 1 AGAIN
```
