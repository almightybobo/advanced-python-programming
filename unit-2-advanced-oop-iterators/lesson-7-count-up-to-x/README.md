# Count Up to X

Build a `CountUpToIterator` that receives a number and counts from 0 up to that number. Example:

```python
iterator = iter(CountUpToIterator(up_to=10))
next(iterator) # 0
next(iterator) # 1
next(iterator) # 2
next(iterator) # 3
# ... Fast Forward ...
next(iterator) # 9
next(iterator) # 10
next(iterator) # StopIteration() Raised!
```
